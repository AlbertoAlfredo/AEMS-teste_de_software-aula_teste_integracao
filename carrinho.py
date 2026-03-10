from produtos import buscar_produto


def adicionar_item(carrinho, produto_id, quantidade):

    produto = buscar_produto(produto_id)

    item = {
        "produto": produto,
        "quantidade": quantidade
    }

    carrinho.append(item)

    return carrinho


def calcular_total(carrinho):

    total = 0

    for item in carrinho:
        total += item["produto"]["preco"] * item["quantidade"]

    desconto = 0

    if total > 500:
        desconto = total * 0.10

    return total - desconto