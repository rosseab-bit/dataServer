from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify, make_response
import pymysql
import sqlite3
import jinja2
import json
import requests
import secrets
from . import routes
import time
import jwt
import datetime
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from packages.dbSqlite import dbSqlite

server=json.loads(open('conf.d/server.json').read())

@routes.route('/register', methods=['POST'])
def signup_user():
    if request.method=='POST':
        data=request.json
        print(data)
        if data['password']==server['access']:
            hashed_password = generate_password_hash(data['password'], method='sha256')
            Public_id=str(uuid.uuid4())
            Username=data['name']
            Password=hashed_password
            Date=str(time.strftime("%Y%m%d%H%M%S"))
            query="insert into Users (Public_id, Username, Password, Date) values ('%s', '%s', '%s', '%s')"%(Public_id, Username, Password, Date)
            print(query)
            sqliteAdmin=dbSqlite()
            if sqliteAdmin.insertDB(query) == 'Insert success':
                return jsonify({'message': 'registered successfully'})
            else:
                return jsonify({'message': 'invalid login password'})


@routes.route('/login', methods=['POST'])
def login():
    if request.method == "POST":
        sqliteAdmin=dbSqlite()
        print(request)
        auth = request.authorization
        print(auth)
        #print(sqliteAdmin.checkUsername(auth.username))
        user_data=list(sqliteAdmin.checkUsername(auth.username))
        #print(len(user_data))
        #print(user_data[2])
        #print(auth)
        #print(datetime.datetime.utcnow() + datetime.timedelta(minutes=30))
        #print(check_password_hash(user_data[2], auth.password))
        if not auth or not auth.username or not auth.password:
            return make_response('could not verify(no hay datos)', 401, {'WWW.Authentication': 'Basic realm: "login required"'})
        #user = Users.query.filter_by(name=auth.username).first()

        if len(user_data)==0:
            return make_response('could not verify(fallo en longitud de lista)', 401, {'WWW.Authentication': 'Basic realm: "login required"'})

        if check_password_hash(user_data[3], auth.password):
            token = jwt.encode({'public_id': user_data[1], 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, server['secret_key'])
            return jsonify({'token' : token})

    return make_response('could not verify(fallo todo)',  401, {'WWW.Authentication': 'Basic realm: "login required"'})
