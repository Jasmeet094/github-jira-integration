# GitHub to Jira Ticket Creator using Python 
## Description
This project aims to streamline the process of creating Jira tickets from GitHub issues. Developers can simply comment "/CreateJira" on their GitHub issues, and this Flask application will automatically create corresponding Jira tickets. This reduces the overhead for developers to track issues in GitHub and simultaneously create Jira tickets for DevOps teams.

## Note:

```
There are 2 files "main.py" & "create_jira.py". Difference between these 2 files is that "main.py" file will create the app to use any comment starting with Slash "/" to create Jira tickets meaning anyone can comment any word with / and the jira ticket will be created. But the file "create_jira.py" will only create tickets with word "/CreateJira" only. No other words starting with "/" will create tickets.
```


## Resources:

[Python Code to Create Issue in Jira ](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-rest-api-3-issue-post)



## How this Works

I have created a Github webhook which will send a payload (which will contain all the information who commented "/JiraCreate") in issues to Python Flask application running on Ec2. and then the python app send POST request to JIRA and it will create a ticket in the project.

## Prerequisites
- #### Before running this application, ensure you have the following installed/configured:

1. An AWS EC2 instance
2. Create a free Jira Atlassian Account and Create a project in which you want to create a ticket
3. Python 3.10.12
4. Flask (pip3 install Flask)
5. GitHub account with access to repository issues
6. Jira account with access to create tickets and API token

## Steps


### 1. Configure Jira API Token:
```
1. Create a Project (Kanban/Scrum)
2. Go to profile and then manage account
3. Go to security tab and Generate a API Token and save it securely.
4. Replace the placeholder API token in the Python code with your actual API token and also replace url of your atlassian account and email.

```


### 2. Create AWS EC2 instance
```
1. Create a EC2 Instance of type t2.micro (Ubuntu 22.04) 
2. Python is already installed in this if not install
3. Open inbound rules to allow all traffic for 0.0.0.0
4. Grab/Copy Public IPv4 DNS of the ec2 instance which should be like 'ec2-13-127-105-246.ap-south-1.compute.amazonaws.com'
5. sudo apt-get update
6. sudo apt-get -y install python3-pip
7. pip install Flask
8. Copy the main.py file and Run the Flask application on your EC2 instance by using this command "python3 main.py" so we can activate the github webhook.
9. You can also verify in this meantime a ticket will be got created in your project.


```



### 3. Configure GitHub Webhook:
```
1. Go to your GitHub repository settings.
2. Navigate to "Webhooks" on the left side panel and add a new webhook.
3. Paste the Payload URL to your EC2 instance address where the Flask application is hosted for ex: http://ec2-13-127-105-246.ap-south-1.compute.amazonaws.com:5000/CreateJira
4. Set the content type to application/json.
5. Choose the individual events to trigger the webhookand select issue comments.
6. Add the webhook and ensure it's active. (make sure application is running to activate the webhook)
7. The application should now be running and ready to receive payloads from GitHub.

```

###  4. Testing:

```
1. Create a test issue in your GitHub repository.
2. Comment /CreateJira on the issue.
3. Check your Jira project for the corresponding ticket created automatically.
  WoooHoooo!!!! You have made it



```
