from flask import Blueprint, jsonify, request
from models.pedido import Pedido
from views.pedido_view import pedido_to_json, pedidos_list_to_json
from database import db

pedido_bp = Blueprint("pedido", __name__)

@pedido_bp.route("/pedido/<int:id>" , methods=["GET"])
def get_pedido(id):
    pedido = Pedido.query.get_or_404(id)
    print(pedido)
    return jsonify( pedido_to_json(pedido) )


@pedido_bp.route("/pedidos", methods=["GET"])
def get_pedidos():
    pedidos = Pedido.query.all()
    return jsonify(pedidos_list_to_json(pedidos))


@pedido_bp.route("/pedido/create", methods=["POST"])
def create_pedido():
    data = request.json
    new_pedido = Pedido(id_pedido=data["id_pedido"], id_produto=data["id_produto"], id_cliente=data["id_cliente"], qtd=data["qtd"])
    db.session.add(new_pedido)
    db.session.commit()
    return jsonify({"message": "pedido criado com sucesso!"}) ,201


@pedido_bp.route("/pedido/updateAll/<int:id>", methods=["PUT"])
def update_all_fields_pedido(id):
    pedido = Pedido.query.get_or_404(id)
    data = request.json
    pedido.id_pedido = data["id_pedido"]
    pedido.id_produto = data["id_produto"]
    pedido.id_cliente = data["id_cliente"]
    pedido.qtd = data["qtd"]
    db.session.commit()
    return jsonify({"message": "pedido atualizado com sucesso!"})

@pedido_bp.route("/pedido/update/<int:id>", methods=["PATCH"])
def update_pedido(id):
    pedido = Pedido.query.get_or_404(id)
    data = request.json
    pedido.id_pedido = data["id_pedido"]
    pedido.id_produto = data["id_produto"]
    pedido.id_cliente = data["id_cliente"]
    pedido.qtd = data["qtd"]
    db.session.commit()
    return jsonify({"message": "pedido atualizado com sucesso!"})



@pedido_bp.route("/pedido/delete/<int:id>", methods=["DELETE"])
def delete_pedido(id):
    pedido = Pedido.query.get_or_404(id)
    db.session.delete(pedido)
    db.session.commit()
    return jsonify({"message": "pedido deletado com sucesso!"})


@pedido_bp.route("/pedido/count", methods=["GET"])
def count_pedidos():
    count = Pedido.query.count()
    return jsonify({"count": count})

@pedido_bp.route("/pedido/id_pedido/<int:id_pedido>", methods=["GET"])
def get_pedido_by_idpedido(id_pedido):
    pedido = None
    pedido = pedido.query.filter_by(id_pedido=id_pedido).first()
    
    if pedido is None:
        return jsonify({"message": "pedido não encontrado!"}), 404
    
    return jsonify(pedido_to_json(pedido))

