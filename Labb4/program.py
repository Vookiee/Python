from flask import Flask, render_template, jsonify
from flask import request
import sqlite3
import json

app = Flask(__name__,template_folder='index')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/volkan', methods =['GET'])
def signup(data= None):
    hej = sqlite3.connect('signup.db')
    volkan = hej.cursor()
    volkan.execute('SELECT fornamn, id FROM users')
    users = volkan.fetchall()
    nousers = len(users)
    return render_template('index.html', username = data, users = users, len = nousers)

@app.route('/', methods = ['POST'])
def volkan():
    print(request.form)
    return { 'status' : f'Added user with username: {request.form.get("fornamn")}' }
