#!/bin/bash
path_repo=`pwd`
sudo docker build -t xymon_app .
sudo docker run -v "$path_repo"/database:/data_xymon/database -v "$path_repo"/tmp:/data_xymon/tmp  -p 3000:3000 xymon_app
