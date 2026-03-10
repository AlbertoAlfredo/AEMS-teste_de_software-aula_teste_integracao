usuarios = []


def cadastrar_usuario(nome, email):

    if "@" not in email:
        print("Email inválido")

    usuarios.append({
        "nome": nome,
        "email": email
    })


def buscar_usuario(email):

    for u in usuarios:
        if u["email"] == email:
            return u

    return False