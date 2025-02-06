from flask import Blueprint, redirect, jsonify

cliente_bp = Blueprint("cliente", __name__)

@cliente_bp.route("/cliente" , methods=["GET"])
def index():
    return jsonify({ "message":" Esta é API com as funções de Cliente"})