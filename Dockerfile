FROM python:2
COPY postmessage.py /
COPY requirements.txt / 
COPY event.json /github/workflow/event.json
WORKDIR /
RUN pip install -r requirements.txt
CMD ["python", "/postmessage.py"]