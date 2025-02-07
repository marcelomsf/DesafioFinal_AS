def produto_to_json(produto):
    return {
        "id": produto.id,
        "nome": produto.nome,
        "descricao" : produto.descricao,
        "valor": produto.valor
        
    }

def produtos_list_to_json(produtos):
    return [produto_to_json(produto) for produto in produtos]
