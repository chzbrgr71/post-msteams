import pymsteams
import sys
import os
import json

# import json payload
#file_path = 'issue-comment-event.json'
file_path = '/github/workflow/event.json'

with open(file_path, 'r') as read_file:
    data = json.load(read_file)

# event type for Action must be specified
eventType = os.environ['GH_EVENT_TYPE']

if eventType == 'push':
    account = data['pusher']['name']
    message = 'Commit to GitHub by ' + account
    url = data['compare']
elif eventType == 'pull_request':
    message = 'PR submitted to Github: ' + data['pull_request']['title']
    url = data['pull_request']['html_url']
elif eventType == 'issue':
    message = 'New/updated GitHub issue: ' + data['issue']['title']
    url = data['issue']['html_url']
elif eventType == 'issue_comment':
    message = 'A Github issue comment was posted: ' + data['comment']['body']
    url = data['issue']['html_url']

# You must create the connectorcard object with the Microsoft Webhook URL
myTeamsMessage = pymsteams.connectorcard(os.environ['TEAMS_WEBHOOK_URL'])

# Add text to the message
myTeamsMessage.text(message)
myTeamsMessage.addLinkButton('Github Link', url)

# send the message.
myTeamsMessage.send()