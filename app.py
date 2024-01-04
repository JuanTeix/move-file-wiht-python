from flask import Flask
from moveFile import moveFile

app = Flask(__name__)


@app.route('/activar')
def activar():
    return moveFile()
     
