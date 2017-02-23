import urllib
import jinja2
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)
app.jinja_loader = jinja2.FileSystemLoader('/app/')


@app.route('/')
def hello_world():

    return render_template('dole.html')

if __name__ == '__main__':
    app.run(port=5002,debug=True,host='0.0.0.0')
