# -*- coding: utf-8 -*-
import time
import json


def formatJSON():
    dataRed=open('/home/hunter/Escritorio/developer/github/data_xymon/tmp/dataRed.txt')
    dataYellow=open('/home/hunter/Escritorio/developer/github/data_xymon/tmp/dataYellow.txt')
    dataGreen=open('/home/hunter/Escritorio/developer/github/data_xymon/tmp/dataGreen.txt')
    json_data={"red":[],
                "yellow":[],
                "green":[]}
    red=[]
    yellow=[]
    green=[]
    alarm={}
    for line in dataRed:
        alert=line.split('|')[1]
        alarm[line.split('|')[0]]= alert.rstrip('\n')
        red.append(alarm)
        alarm={}

    for line in dataYellow:
        alert=line.split('|')[1]
        alarm[line.split('|')[0]]= alert.rstrip('\n')
        yellow.append(alarm)
        alarm={}

    for line in dataGreen:
        alert=line.split('|')[1]
        alarm[line.split('|')[0]]= alert.rstrip('\n')
        green.append(alarm)
        alarm={}

    json_data['red']=red
    json_data['yellow']=yellow
    json_data['green']=green
    #writeJson=open('', 'w')
    with open('/home/hunter/Escritorio/developer/github/data_xymon/database/db.json', 'w') as file:
        json.dump(json_data, file, indent=4)
    return 'alarms success'

#formatJSON()
