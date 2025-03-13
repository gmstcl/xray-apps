FROM python:alpine

COPY . .
RUN pip3 install aws-xray-sdk && pip3 install flask
CMD ["python3","app.py"]
