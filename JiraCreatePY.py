import requests
from requests.auth import HTTPBasicAuth

def create_jira_ticket():
    # nahradiť realnou adresou
    create_issue_url = "https://your-jira-instance/rest/api/2/issue/"

    jira = input("Jira Ticket Creation, continue")
    username = input("Enter your Jira username: ")
    password = input("Enter your Jira password: ")
    project_key = input("Enter the Jira project key: ")
    summary = input("Enter a short summary of the issue: ")
    environment = input("Enter the environment (Playground, Preprod, Prod, QA): ")
    hub_name = input("Enter the hub name: ")
    team_name = input("Enter the name of the team in MissionControl: ")
    api_usage = input("Enter API usage (Provider, Consumer): ")
    platform_used = input("Enter the TARDIS Platform used (AWS, CaaS@DTIT, Cetus, Canis): ")
    description = input("Enter the full description of the issue: ")
    reproduce_steps = input("Enter optional steps to reproduce the issue (if any): ")
    expected_behavior = input("Enter optional expected behavior (if any): ")

    issue_data = {
        "fields": {
            "project": {"key": project_key},
            "summary": summary,
            "description": description,
            "issuetype": {"name": "Bug"},  # Change this to the appropriate issue type
            "customfield_12345": environment,  # Replace with the actual custom field ID for environment
            "customfield_67890": hub_name,  # Replace with the actual custom field ID for hub name
            "customfield_11111": team_name,  # Replace with the actual custom field ID for team name
            "customfield_22222": api_usage,  # Replace with the actual custom field ID for API usage
            "customfield_33333": platform_used,  # Replace with the actual custom field ID for platform used
            "customfield_44444": reproduce_steps,  # Replace with the actual custom field ID for reproduce steps
            "customfield_55555": expected_behavior  # Replace with the actual custom field ID for expected behavior
        }
    }

    response = requests.post(
        create_issue_url,
        json=issue_data,
        auth=HTTPBasicAuth(username, password),
        headers={"Content-Type": "application/json"}
    )

    if response.status_code == 201:
        print("Issue created successfully!")
        print("Issue Key:", response.json()["key"])
    else:
        print("Failed to create issue. Status code:", response.status_code)
        print("Response:", response.text)
