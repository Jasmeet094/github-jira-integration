from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json

# create flask app instance 

app = Flask(__name__)

@app.route("/JiraCreate". methods=['POST'])

def createjira():
    

        url = "https://jasmeet.atlassian.net/rest/api/3/issue"

        auth = HTTPBasicAuth("cikac29946@fryshare.com", "ATATT3xFfGF0__UYe6YCCc4eMGUILfM8s3pxEkkrrh7guHxLI_PVYRwCjxg8ShOgc2HukaPiFIhjDDI1XdhS73bYekerQvuxu58e6DGvx6HLddEMqbXNSxRNUeT2FlrSTvM9dtP3XOaV48-8hoeTKPHDsoD_R0l9gO5EGQx2qOeCEYX_9itQeOM=8BAD092C")

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
