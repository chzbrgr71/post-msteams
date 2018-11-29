import pymsteams
import sys
import os

# You must create the connectorcard object with the Microsoft Webhook URL
myTeamsMessage = pymsteams.connectorcard(os.environ['TEAMS_WEBHOOK_URL'])

# Add text to the message.
myTeamsMessage.text(os.environ['TEAMS_MESSAGE'])

# send the message.
myTeamsMessage.send()