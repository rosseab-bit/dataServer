#!/bin/bash
path_repo=`pwd`
sudo docker build -t data_server_app .
sudo docker run -v "$path_repo"/database:/dataServer/database -v "$path_repo"/tmp:/dataServer/tmp  -p 3000:3000 data_server_app
