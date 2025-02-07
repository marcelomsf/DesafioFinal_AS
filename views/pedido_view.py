def pedido_to_json(pedido):
    return {
        "id": pedido.id,
        "id_pedido": pedido.id_pedido,
        "id_produto" : pedido.id_produto,
        "id_cliente": pedido.id_cliente,
        "qtd": pedido.qtd
        
    }

def pedidos_list_to_json(pedidos):
    return [pedido_to_json(pedido) for pedido in pedidos]

