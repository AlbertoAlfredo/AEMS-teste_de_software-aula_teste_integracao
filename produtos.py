produtos = {
    1: {"nome": "Notebook", "preco": 3500, "estoque": 5},
    2: {"nome": "Mouse", "preco": 80, "estoque": 20},
    3: {"nome": "Teclado", "preco": 150, "estoque": 10}
}


def buscar_produto(id):
    return produtos[id]


def atualizar_estoque(id, quantidade):
    produto = produtos[id]
    produto["estoque"] = produto["estoque"] - quantidade