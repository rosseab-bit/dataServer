from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify, make_response
import pymysql
import sqlite3
import jinja2
import json
import requests
import secrets
import datetime
from . import routes
from functools import wraps
from packages.tokenValidator import token_required
from packages.formatDataJSON import formatJSON
@routes.route('/dataxymon', methods=['GET'])
@token_required
def dbGet(current_user):
    if request.method == "GET":
        formatJSON()
        db=json.loads(open('database/db.json').read())
    return jsonify(db)
