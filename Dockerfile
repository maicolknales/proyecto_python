FROM python:3.6.9-alpine
WORKDIR /project
ADD . /project
ENV DB_CON=mysql+pymysql://root:Barcelona1@localhost:3306/FACTURACIONDB
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python","App.py"]