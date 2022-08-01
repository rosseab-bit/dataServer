from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
import pymysql
import sqlite3
import jinja2
import requests
import secrets
from routes import *
from flask import Blueprint
from functools import wraps

app = Flask(__name__)
server=json.loads(open('conf.d/server.json').read())
app.secret_key=server['secret_key']
app.register_blueprint(routes)



if __name__ == '__main__':
        app.jinja_env.filters['zip'] = zip
        app.run(host=server['server']['host'], port=server['server']['port'], debug = True)
