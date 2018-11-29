import pymsteams
import sys
import os
import json

# You must create the connectorcard object with the Microsoft Webhook URL
myTeamsMessage = pymsteams.connectorcard(os.environ['TEAMS_WEBHOOK_URL'])

with open('/github/workflow/event.json', 'r') as read_file:
    data = json.load(read_file)

message = 'A Github issue comment was posted. ' + data['comment']['body']

# Add text to the message
myTeamsMessage.text(message)
myTeamsMessage.addLinkButton('Link to Github comment', data['issue']['html_url'])


# send the message.
myTeamsMessage.send()