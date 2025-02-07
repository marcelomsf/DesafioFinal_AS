from flask import Blueprint, jsonify, request
from models.produto import Produto
from views.produto_view import produto_to_json, produtos_list_to_json
from database import db

produto_bp = Blueprint("produto", __name__)

@produto_bp.route("/produto/<int:id>" , methods=["GET"])
def get_cliente(id):
    produto = Produto.query.get_or_404(id)
    print(produto)
    return jsonify( produto_to_json(produto) )


@produto_bp.route("/produtos", methods=["GET"])
def get_produtos():
    produtos = Produto.query.all()
    return jsonify(produtos_list_to_json(produtos))


@produto_bp.route("/produto/create", methods=["POST"])
def create_produto():
    data = request.json
    new_produto = Produto(nome=data["nome"], descricao=data["descricao"], valor=data["valor"])
    db.session.add(new_produto)
    db.session.commit()
    return jsonify({"message": "Produto criado com sucesso!"}) ,201


@produto_bp.route("/produto/updateAll/<int:id>", methods=["PUT"])
def update_all_fields_produto(id):
    produto = Produto.query.get_or_404(id)
    data = request.json
    produto.nome = data["nome"]
    produto.descricao = data["descricao"]
    produto.valor = data["valor"]
    db.session.commit()
    return jsonify({"message": "Produto atualizado com sucesso!"})

@produto_bp.route("/produto/update/<int:id>", methods=["PATCH"])
def update_produto(id):
    produto = Produto.query.get_or_404(id)
    data = request.json
    produto.nome = data["nome"]
    produto.descricao = data["descricao"]
    produto.valor = data["valor"]
    db.session.commit()
    return jsonify({"message": "Produto atualizado com sucesso!"})



@produto_bp.route("/produto/delete/<int:id>", methods=["DELETE"])
def delete_produto(id):
    produto = Produto.query.get_or_404(id)
    db.session.delete(produto)
    db.session.commit()
    return jsonify({"message": "Produto deletado com sucesso!"})


@produto_bp.route("/produto/count", methods=["GET"])
def count_produtos():
    count = Produto.query.count()
    return jsonify({"count": count})

@produto_bp.route("/produto/nome/<string:nome>", methods=["GET"])
def get_produto_by_nome(nome):
    produto = None
    produto = Produto.query.filter_by(nome=nome).first()
    
    if produto is None:
        return jsonify({"message": "Produto não encontrado!"}), 404
    
    return jsonify(produto_to_json(produto))

