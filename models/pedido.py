from database import db


class Pedido(db.Model):
    #id, username, nome, email, endereco
    id = db.Column(db.Integer )
    id_pedido = db.Column(db.Integer)
    id_produto = db.Column(db.Integer,nullable=False)
    id_cliente = db.Column(db.Integer, unique=True, nullable=False)
    qtd = db.Column(db.String(200),  nullable=False)

