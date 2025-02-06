from database import db
from flask_login import UserMixin

class Cliente(db.Model, UserMixin):
    #id, username, nome, email, endereco
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    nome = db.Column(db.String(200),  nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    endereco =  db.Column(db.Text, unique=True, nullable=True)
    