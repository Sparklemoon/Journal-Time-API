from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy   
from flask_marshmallow import Marshmallow
from flask_cors import CORS    
from flask_heroku import Heroku
from flask_bcrypt import Bcrypt  

import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"]=''

db = SQLAlchemy(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)


Heroku(app)
CORS(app)

class User(db.Model):
    id = db.Column(db.Integer, primry_key=True)
    email = db.Column(db.String(20), unique=True, nullable=False)
    password =db.Column(db.String, nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password = password

class UserSchema(ma.Schema):
    class Meta:
        feilds=("id", "email", "password")

user_schema = UserSchema()
multiple_user_schema = UserSchema(many=True)

class Journal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person = db.Column(db.String, nullable=True)
    title = db.Column(db.String, nullable=True)
    description = db.Column(db.String, nullable=False, unique=True)
    date = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=True)

    def __init__(self, person, title, description, date, location)
        self.person = person
        self.title = title
        self.description = description
        self.date = date
        self.location = location

class JournalSchema(ma.Schema):
    class Meta: 
        feilds = ("id", "person", "title", "description", "date", "location")

journal_schema = JournalSchema()
multiple_journal_schema = JournalSchema(many=True)       

@app.route("/user/add", methods=["POST"])
def create_user():
    if request.content_type !="aplication/json":
        return "YOU NEED JSON!!!"

    post_data = request.get_json()
    email = post_data.get("email")
    password = post_data.get("password")

    record = User(email, password)
    db.session.add(record)
    db.session.commit()

    return jsonify("Data added good job")

    existingUser = db.session.query(User).filter(User.username == username).first()
    if existingUser is not None:
        return jsonify("User already exists")

    password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

@app.route("/journal/add", methods=["POST"])
def create_journal():
    if request.content_type !="aplication/json":
        return "YOU NEED JSON!!!"

    post_data = request.get_json()
    person = post_data.get("person")
    title = post_data.get{"title"}
    description = post_data.get("description")
    date = post_data.get("date")
    location = post_data.get("location")

    record = Journal(person, title, description, date, location)
    db.session.add(record)
    db.session.commit()

    return jsonify("Data added successfully")

@app.route("/user/get", methods=["GET"])
def get_all_users():
    all_users = db.session.query(User).all()
    return jsonify(multiple_users_schema.dump(all_users))


@app.route("/user/get/<id>", methods=["GET"])
def get_one_user(id):
    one_user = db.session.query(User).fiter(User.id == id).first()
    return jsonify(user_schema.dump(one_user))

@app.route("/user/journal/<user_id>/<journal_id>", methods=["GET"])
def get_one_users_journal(user_id, journal_id):
    user = db.session.query(User).filter(User.id == user_id).first()
    journal = db.session.query(Journal).filter(Journal.id == journal_id).first()
    result = [user_schema.dump(user), journal_schema.dump(journal)]
    return jsonify(result)

@app.route("/user/delete/<user>", methods=["DELETE"])
def delete_user_journal_by_id(id):
    record = db.session.query(User).filter(User.email == email).first()
    if record is None:
        return jsonify("User does not exist")

@app.route("/user/delete/<journal>", methods=["DELETE"])
def delete_user_journal_by_id(id):
    record = db.session.query(Journal).filter(User.journal == journal).first()
    if record is None:
        return jsonify("Journal does not exist")

    db.session.delete(record)
    db.session.commit()
    return jsonify("Journal was successfully deleted")



if __name__ == "__main__":
    app.run(debug=True)
