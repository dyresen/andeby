FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
COPY ./requirements.txt /app/requirements.txt
COPY ./dole.html /app/dole.html
COPY ./dole-duck.png /app/dole-duck.png
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
