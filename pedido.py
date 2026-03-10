from carrinho import calcular_total
from produtos import atualizar_estoque


def finalizar_pedido(carrinho):

    total = calcular_total(carrinho)

    for item in carrinho:

        produto_id = item["produto"]["nome"]

        atualizar_estoque(produto_id, item["quantidade"])

    return {
        "status": "confirmado",
        "total": total
    }