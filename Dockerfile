FROM python:3.6.9-alpine
WORKDIR /project
ADD . /project
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python","App.py"]