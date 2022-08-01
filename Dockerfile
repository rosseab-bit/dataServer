FROM python:3.9.13-alpine3.15
WORKDIR /dataServer
COPY . .
RUN pip install -r /dataServer/conf.d/requeriments.txt
CMD ["python3", "/data_xymon/app.py"]
