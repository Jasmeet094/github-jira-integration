# This code allows any comment starting with '/' in GitHub issues to create tickets in Jira. To make app only create tickets with specific comment "/CreateJira" follow the code in create_jira.py
from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json

# create flask app instance

app = Flask(__name__)

@app.route("/CreateJira", methods=['POST'])

def createjira():

    url = "https://jasmeet.atlassian.net/rest/api/3/issue"

    auth = HTTPBasicAuth("cikac29946@fryshare.com", "ATATT3xFfGF0qxPbR-PV-9L41fjHIpas-wb_uGMAUlhKZQK8luL0puP1r_tlnGw9tD06HH4hL73zMOMrkaXgjgNaks15zqWxv4cIIuv0Wfdp-K8gykU5ovjXmufbdnu9-LXeL5EUmKRRoNQtsVvRIs-zrx89FpmEgZytR4YVOmGUnrTt_c6ijYw=CA29E67F")

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {



    "description": {
      "content": [
        {
          "content": [
            {
              "text": "my first ticket.",
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

    "summary": "DEMO Ticket",

    },
    "update": {}
    } )

    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )

    return(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


app.run('0.0.0.0' , port=5000)
