FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
COPY ./requirements.txt /app/requirements.txt
COPY ./ole.html /app/ole.html
COPY ./ole-duck.png /app/ole-duck.png
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
