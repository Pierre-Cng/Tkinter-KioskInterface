from jira import JIRA

# Jira server URL and credentials
JIRA_SERVER = r'https://server.atlassian.net/'
USERNAME = ''
PASSWORD = ''

# Connect to Jira
jira = JIRA(server=JIRA_SERVER, basic_auth=(USERNAME, PASSWORD))

# Issue details
project_key = ''  # Replace with your project key
issue_type = 'Task'  # Replace with the issue type you want to create
summary = 'Test'  # Replace with the summary of your issue
description = 'testing'  # Replace with the description of your issue

# Create the issue
issue_dict = {
    'project': {'key': project_key},
    'summary': summary,
    'description': description,
    'issuetype': {'name': issue_type},
}

new_issue = jira.create_issue(fields=issue_dict)
print(f"Created issue: {new_issue.key}")
