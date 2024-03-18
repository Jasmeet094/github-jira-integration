from flask import Flask, request, jsonify
from requests.auth import HTTPBasicAuth
import requests  # Import requests module here
import json

app = Flask(__name__)

@app.route("/CreateJira", methods=['POST'])
def handle_webhook():
    payload = request.json
    
    # Check if the comment contains the trigger '/CreateJira'
    if 'comment' in payload and '/CreateJira' in payload['comment']['body']:
        create_jira_ticket(payload)
        return jsonify({'message': 'Jira ticket created successfully'}), 200
    else:
        return jsonify({'message': 'No action taken. Trigger not found'}), 200

def create_jira_ticket(payload):
    url = "https://jasmeet.atlassian.net/rest/api/3/issue"
    auth = HTTPBasicAuth("cikac29946@fryshare.com", "ATATT3xFfGF0USyiMrxrysOsO2Ro80UxIkdGg1whLXHj0pvYfNTPHgKQoTUmV1tW8aKFsj_FGG0O1BPjHQ1wXnRbyG1e5nERquoUDoWU9DdbYtt5wFPDcwgdQJbLPHnz4gQYy-PILD72P0Ik2uY3OWNCgVPypQuB4L9Hmr_it7zfOjGelOlL38U=90309FAB")
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    issue_url = payload.get('issue', {}).get('html_url', 'N/A')
    issue_title = payload.get('issue', {}).get('title', 'N/A')
    payload = {
        "fields": {
            "description": {
                "content": [
                    {
                        "content": [
                            {
                                "text": "Integration test from github to Jira",
                                "type": "text"
                            }
                        ],
                        "type": "paragraph"
                    }
                ],
                "type": "doc",
                "version": 1
            },
            "issuetype": {
                "id": "10001"
            },
            "project": {
                "key": "MFK"
            },
            "summary": "Test Ticket Created from Github Issues"
        },
        "update": {}
    }
    response = requests.post(
        url,
        json=payload,
        headers=headers,
        auth=auth
    )
    print(response.json())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
