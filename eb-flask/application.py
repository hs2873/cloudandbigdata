
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing
import mysql.connector


# create app
application = Flask(__name__)
application.config["DEBUG"]=True


# apis

def get_data(url, genre, email):
    url = "https://www.googleapis.com/books/v1/volumes?q=" + request.form["user_search"]
    response_dict = requests.get(url).json()
    return



@application.route('/twitthmp/<filter>',methods=['POST','GET'])
def twitthmp(filter):
    if request.method == 'POST':
        get_data()
    return render_template('index.html')


@application.route('/twitthmp')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    application.debug=True
    application.run()
