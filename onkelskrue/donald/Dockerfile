FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
COPY ./requirements.txt /app/requirements.txt
COPY ./donald.html /app/donald.html
COPY ./donald-duck.png /app/donald-duck.png
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
