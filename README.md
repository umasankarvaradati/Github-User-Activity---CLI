# GitHub User Activity CLI Tool

This command-line tool fetches and displays recent activity for a specified GitHub user. It groups events by repository and provides a summary of different event types such as pushes, pull requests, issues, comments, and more.

## Features

- Fetches recent public events from the GitHub API for a given username.
- Groups events by repository.
- Counts and displays occurrences of various event types:
  - PushEvent
  - PullRequestEvent
  - IssuesEvent
  - IssueCommentEvent
  - WatchEvent (stars)
  - PullRequestReviewEvent
  - PullRequestReviewCommentEvent
  - CreateEvent

## Requirements

- Python 3.6+
- `requests` library
- `rich` library (for colored and formatted console output)

## Installation

1. Clone the repository or download the script.
2. Install dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage

Run the tool with a GitHub username as an argument using the provided batch file (for Windows):

```bash
github-activity <GitHubUsername>
```

Example:

```bash
github-activity umasankarvaradati
```

**Note for Windows users:** Use the `github-activity.bat` file to run the tool, which sets up the virtual environment automatically.

## Output

The script will print a summary of the user's recent GitHub activity grouped by repository. Here are some sample outputs:

### Example 1: Active Developer
```
➡️  Pushed 5 commits to umasankarvaradati/Task-tracker-CLI
➡️  Created 2 pull request(s) for umasankarvaradati/All_at_one
➡️  Commented on 3 issue(s) on umasankarvaradati/Process-Monitoring-Agent-with-Django
➡️  Reviewed 1 pull request(s) for umasankarvaradati/Task-tracker-CLI
```

### Example 2: Repository Creator
```
➡️  Created repo umasankarvaradati/New-Project
➡️  Pushed 1 commit(s) to umasankarvaradati/New-Project
➡️  Starred octocat/Hello-World
```

### Example 3: Issue Handler
```
➡️  Opened 2 new issue(s) in umasankarvaradati/Bug-Tracker
➡️  Commented on 4 issue(s) on umasankarvaradati/Bug-Tracker
➡️  Created 1 pull request(s) for umasankarvaradati/Bug-Tracker
```

## Error Handling

If the username is invalid or there is an issue fetching data from GitHub, an error message will be displayed.

## License

This project is licensed under the MIT License.

---

Inspired from [GitHub User Activity Project](https://roadmap.sh/projects/github-user-activity)
