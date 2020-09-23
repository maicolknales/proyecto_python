FROM python:3.6.9-alpine
WORKDIR /project
ADD . /project
RUN pip3 install -r requirements.txt
CMD ["python3","App.py"]