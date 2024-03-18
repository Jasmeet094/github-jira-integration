# GitHub to Jira Ticket Creator using Python 
## Description
This project aims to streamline the process of creating Jira tickets from GitHub issues. Developers can simply comment "/JiraCreate" on their GitHub issues, and this Flask application will automatically create corresponding Jira tickets. This reduces the overhead for developers to track issues in GitHub and simultaneously create Jira tickets for DevOps teams.

Resources:

[Python Code to Create Issue in Jira ](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-rest-api-3-issue-post)



## How this Works

I have created a Github webhook which will send a payload (which will contain all the information who commented "/JiraCreate") in issues to Python Flask application running on Ec2. and then the python app send POST request to JIRA and it will create a ticket in the project.

## Prerequisites
- #### Before running this application, ensure you have the following installed/configured:

1. An AWS EC2 instance running with Python installed
2. Create a free Jira Atlassian Account and Create a project in which you want to create a ticket
3. Python 3.x
4. Flask (pip install Flask)
5. Requests (pip install requests)
6. GitHub account with access to repository issues
7. Jira account with access to create tickets and API token

## Steps
- #### Follow these steps to set up and run the Flask application:

### Clone Repository: Clone this repository to your local machine.
```
bash
Copy code
git clone <repository_url>
Install Dependencies: Navigate to the project directory and install the required dependencies using pip.

bash
Copy code
cd <project_directory>
pip install -r requirements.txt

```

### Configure GitHub Webhook:
```
Go to your GitHub repository settings.
Navigate to "Webhooks" and add a new webhook.
Set the Payload URL to your EC2 instance address where the Flask application is hosted.
Set the content type to application/json.
Choose the events to trigger the webhook (e.g., issue comments).
Add the webhook and ensure it's active.
```

### Configure Jira API Token:
```
1. Create a Project (Kanban/Scrum)
2. Go to profile and then manage account
3. Go to security tab and Generate a API Token and save it securely.
4. Replace the placeholder API token in the Python code with your actual API token and also replace url of your atlassian account and email.

```

Run Flask Application:

Run the Flask application on your EC2 instance.
bash
Copy code
python app.py
The application should now be running and ready to receive payloads from GitHub.

Testing:

Create a test issue in your GitHub repository.
Comment /JiraCreate on the issue.
Check your Jira project for the corresponding ticket created automatically.
Deployment:

For production deployment, consider using a production-ready web server like Gunicorn or deploying to a platform like AWS Elastic Beanstalk.
