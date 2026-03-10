from carrinho import adicionar_item
from pedido import finalizar_pedido

carrinho = []

adicionar_item(carrinho, 1, 1)
adicionar_item(carrinho, 2, 2)

pedido = finalizar_pedido(carrinho)

print(pedido)