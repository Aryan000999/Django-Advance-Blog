FROM python:3.14

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 

WORKDIR /app
COPY requrements.txt /app/


RUN pip3 install -r requrements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY ./core /app/
