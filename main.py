"""
GitHub User Activity CLI Tool

This script fetches and displays recent activity for a given GitHub username.
It groups events by repository and provides a summary of different event types.
"""

import argparse
import requests
from collections import defaultdict
from rich import print as rich_print


def fetch_user_events(username):
    """
    Fetch recent events for a GitHub user.

    Args:
        username (str): The GitHub username.

    Returns:
        list: List of event dictionaries from the GitHub API.
    """
    api_url = f"https://api.github.com/users/{username}/events"
    headers = {
        'X-GitHub-Api-Version': '2022-11-28',
        "accept": "application/vnd.github+json"
    }
    response = requests.get(api_url, headers=headers)
    if response.status_code != 200:
        raise ValueError(f"Error fetching events for {username}: {response.status_code}")
    return response.json()


def group_events_by_repo(events):
    """
    Group events by repository and count event types.

    Args:
        events (list): List of event dictionaries.

    Returns:
        dict: Dictionary with repo names as keys and event counts as values.
    """
    user_events = defaultdict(lambda: defaultdict(int))
    for event in events:
        repo_name = event['repo']['name']
        event_type = event['type']
        user_events[repo_name][event_type] += 1
    return user_events


def display_events(user_events):
    """
    Display the grouped events in a user-friendly format.

    Args:
        user_events (dict): Dictionary of events grouped by repo.
    """
    for repo, events in user_events.items():
        for event, count in events.items():
            if event == 'IssueCommentEvent':
                rich_print(f":arrow_right: Commented on {count} issue(s) on {repo}")
            elif event == 'PushEvent':
                rich_print(f":arrow_right: Pushed {count} commit(s) to {repo}")
            elif event == 'IssuesEvent':
                rich_print(f":arrow_right: Opened {count} new issue(s) in {repo}")
            elif event == 'WatchEvent':
                rich_print(f":arrow_right: Starred {repo}")
            elif event == 'PullRequestEvent':
                rich_print(f":arrow_right: Created {count} pull request(s) for {repo}")
            elif event == 'PullRequestReviewEvent':
                rich_print(f":arrow_right: Reviewed {count} pull request(s) for {repo}")
            elif event == 'PullRequestReviewCommentEvent':
                rich_print(f":arrow_right: Commented on {count} pull request(s) for {repo}")
            elif event == 'CreateEvent':
                rich_print(f":arrow_right: Created repo {repo}")
            else:
                rich_print(f":arrow_right: {event}: {count}")


def main():
    """
    Main function to parse arguments and display user activity.
    """
    parser = argparse.ArgumentParser(prog="github-activity", description="Fetch and display GitHub user activity.")
    parser.add_argument('Username', help="The GitHub username to fetch activity for.")
    args = parser.parse_args()

    try:
        events = fetch_user_events(args.Username)
        user_events = group_events_by_repo(events)
        display_events(user_events)
    except ValueError as e:
        rich_print(f"[red]Error:[/red] {e}")

if __name__ == "__main__":
    main()
