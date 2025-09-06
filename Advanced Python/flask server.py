# this is done from flask from internet only to test i don' know anything about this 
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run() # or we can use by flask --app hello run in terminal or by python '.\flask server.py'

#--app hello run this is currently not wokring i don't know why 