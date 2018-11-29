FROM python:2
COPY postmessage.py /
COPY requirements.txt /
WORKDIR /
RUN pip install -r requirements.txt
CMD ["python", "/postmessage.py"]