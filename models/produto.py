from database import db


class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=True, nullable=False)
    descricao = db.Column(db.String(200),  nullable=False)
    valor = db.Column(db.Float(100), unique=True, nullable=False)

    