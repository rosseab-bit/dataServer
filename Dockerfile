FROM ubuntu
WORKDIR /data_xymon
RUN apt-get update && apt-get install -y python3 && apt-get install -y python3-pip
COPY . .
RUN pip3 install -r conf.d/requeriments.txt
CMD ["python3", "/data_xymon/app.py"]
