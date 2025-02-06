from flask import Blueprint, redirect, jsonify, request
from models.cliente import Cliente
from views.cliente_view import clientes_list_to_json, cliente_to_json
from database import db

cliente_bp = Blueprint("cliente", __name__)

@cliente_bp.route("/cliente/<int:id>" , methods=["GET"])
def get_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    print(cliente)
    return jsonify( cliente_to_json(cliente) )


@cliente_bp.route("/clientes", methods=["GET"])
def get_clientes():
    clientes = Cliente.query.all()
    return jsonify(clientes_list_to_json(clientes))


@cliente_bp.route("/cliente/create", methods=["POST"])
def create_cliente():
    data = request.json
    new_cliente = Cliente(username=data["username"], nome=data["nome"], email=data["email"], endereco=data["endereco"])
    db.session.add(new_cliente)
    db.session.commit()
    return jsonify({"message": "Cliente criado com sucesso!"}) ,201


@cliente_bp.route("/cliente/updateAll/<int:id>", methods=["PUT"])
def update_all_fields_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    data = request.json
    cliente.username = data["username"]
    cliente.nome = data["nome"]
    cliente.email = data["email"]
    cliente.endereco = data["endereco"]
    db.session.commit()
    return jsonify({"message": "Cliente atualizado com sucesso!"})

@cliente_bp.route("/cliente/update/<int:id>", methods=["PATCH"])
def update_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    data = request.json
    cliente.username = data.get("username", cliente.username)
    cliente.nome = data.get("nome", cliente.nome)
    cliente.email = data.get("email", cliente.email)
    cliente.endereco = data.get("endereco", cliente.endereco)
    db.session.commit()
    return jsonify({"message": "Cliente atualizado com sucesso!"})


@cliente_bp.route("/cliente/delete/<int:id>", methods=["DELETE"])
def delete_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    return jsonify({"message": "Cliente deletado com sucesso!"})


@cliente_bp.route("/cliente/count", methods=["GET"])
def count_clientes():
    count = Cliente.query.count()
    return jsonify({"count": count})

@cliente_bp.route("/cliente/username/<string:username>", methods=["GET"])
def get_cliente_by_username(username):
    cliente = Cliente.query.filter_by(username=username).first()
    return jsonify(cliente_to_json(cliente))

