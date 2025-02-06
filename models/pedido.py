from database import db
from models.produto import Produto
from models.cliente import Cliente


class Pedido(db.Model):
    #id, username, nome, email, endereco
    id = db.Column(db.Integer, primary_key=True )
    id_pedido = db.Column(db.Integer)
    id_produto = db.Column(db.Integer, db.ForeignKey(Produto.id), nullable=False)
    id_cliente = db.Column(db.Integer, db.ForeignKey(Cliente.id), nullable=False )
    qtd = db.Column(db.String(200),  nullable=False)

