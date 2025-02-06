from flask import Blueprint, redirect, jsonify, request
from models.cliente import Cliente
from database import db

cliente_bp = Blueprint("cliente", __name__)

@cliente_bp.route("/cliente/<int:id>" , methods=["GET"])
def get_cliente(id):
    cliente = Cliente.query.get(id)
    return jsonify({ "id": cliente.id, "username": cliente.username, "nome": cliente.nome, "email": cliente.email, "endereco": cliente.endereco} )


@cliente_bp.route("/clientes", methods=["GET"])
def get_clientes():
    clientes = Cliente.query.all()
    return jsonify([{ "id": cliente.id, "username": cliente.username, "nome": cliente.nome, "email": cliente.email, "endereco": cliente.endereco} for cliente in clientes])


@cliente_bp.route("/cliente/create", methods=["POST"])
def create_cliente():
    data = request.json
    new_cliente = Cliente(username=data["username"], nome=data["nome"], email=data["email"], endereco=data["endereco"])
    db.session.add(new_cliente)
    db.session.commit()
    return jsonify({"message": "Cliente criado com sucesso!"}) ,201

