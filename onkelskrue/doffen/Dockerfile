FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
COPY ./requirements.txt /app/requirements.txt
COPY ./doffen.html /app/doffen.html
COPY ./doffen-duck.gif /app/doffen-duck.gif
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
