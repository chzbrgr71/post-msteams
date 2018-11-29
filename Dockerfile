FROM python:2
COPY postmessage.py /
COPY requirements.txt / 
#COPY event.json /github/workflow/event.json
WORKDIR /
RUN pip install -r requirements.txt
CMD ["python", "/postmessage.py"]

LABEL "com.github.actions.name"="Post to MS Teams"
LABEL "com.github.actions.description"="Action to post messages to a MS Teams channel based on Github issues."
LABEL "com.github.actions.icon"="life-bouy"
LABEL "com.github.actions.color"="yellow"
LABEL "repository"="https://github.com/chzbrgr71/post-msteams"
LABEL "homepage"="https://github.com/chzbrgr71"
LABEL "maintainer"="brianisrunning@gmail.com"