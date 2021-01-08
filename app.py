from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy   
from flask_marshmallow import Marshmallow
from flask_cors import CORS    
from flask_heroku import Heroku
from flask_bcrypt import Bcrypt  

import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"]='postgres://jcqydfrmcbswmt:23ea87404df287326384c16d85b8a77b11851715d05589e9253ccd62d0e11eaf@ec2-35-168-77-215.compute-1.amazonaws.com:5432/d338e1d5sd0shc'

db = SQLAlchemy(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)


Heroku(app)
CORS(app)







if __name__ == "__main__":
    app.run(debug=True)
