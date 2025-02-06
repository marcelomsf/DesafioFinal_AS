def user_to_json(cliente):
    return {
        "id": cliente.id,
        "username": cliente.username,
        "nome" : cliente.nome,
        "email": cliente.email,
        "endereco": cliente.endereco
        
    }

def users_list_to_json(clientes):
    return [user_to_json(cliente) for cliente in clientes]
