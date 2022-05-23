from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
import pymysql
import sqlite3
import jinja2
import json
import requests
import secrets
import time
import jwt
import datetime
import uuid
from functools import wraps
from packages.dbSqlite import dbSqlite
from werkzeug.security import generate_password_hash, check_password_hash
server=json.loads(open('conf.d/server.json').read())

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        print(datetime.datetime.utcnow() + datetime.timedelta(minutes=30))
        token = ''
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']
        if not token:
            return jsonify({'message': 'a valid token is missing'})

        try:
            data = jwt.decode(token, options={"verify_signature": False})
            #print(data)
            sqliteAdmin=dbSqlite()
            current_user=sqliteAdmin.checkPublicId(data['public_id'])[1]
        except:
            return jsonify({'message': 'token is invalid'})
        return f(current_user, *args, **kwargs)
    return decorator
