# Teste de Integração

## 1. O que é Teste de Integração

O **teste de integração** verifica se **diferentes partes de um sistema funcionam corretamente quando combinadas**.

Enquanto o **teste de unidade** valida funções isoladas, o teste de integração valida **a comunicação entre módulos**.

Exemplo de módulos de um sistema:

* Interface do usuário
* API
* Banco de dados
* Serviços externos

O teste de integração garante que **essas partes troquem informações corretamente**.

### Exemplo simples

Imagine um sistema de vendas com dois módulos:

1. cálculo de preço
2. geração de pedido

Mesmo que cada função funcione separadamente, pode ocorrer erro quando elas são usadas juntas.

---

# 2. Diferença entre Teste Unitário e Teste de Integração

| Tipo                | O que testa             |
| ------------------- | ----------------------- |
| Teste unitário      | funções isoladas        |
| Teste de integração | interação entre módulos |
| Teste de sistema    | sistema completo        |

### Exemplo

Funções isoladas:

```python
def calcular_total(preco, quantidade):
    return preco * quantidade

def gerar_pedido(total):
    return f"Pedido gerado com total de R$ {total}"
```

Cada função pode funcionar separadamente.

Mas precisamos testar **a integração entre elas**:

```python
def criar_pedido(preco, quantidade):
    total = calcular_total(preco, quantidade)
    return gerar_pedido(total)
```

Teste de integração:

```python
def test_criar_pedido():
    resultado = criar_pedido(10, 3)
    assert resultado == "Pedido gerado com total de R$ 30"
```

Aqui estamos verificando **a interação entre as duas funções**.

---

# 3. Problemas comuns encontrados em integração

Quando módulos são integrados podem surgir problemas como:

* formatos de dados incompatíveis
* erros de comunicação com APIs
* falhas na conexão com banco de dados
* dependências mal configuradas

Exemplo:

```python
def buscar_usuario(id):
    return {"id": id, "nome": "Ana"}
```

Outro módulo espera:

```python
usuario["name"]
```

Isso gera erro porque o campo correto é **nome**.

Esse tipo de problema só aparece em **testes de integração**.

---

# 4. Estratégias de Teste de Integração

Existem quatro estratégias principais.

---

## 4.1 Big Bang

Todos os módulos são integrados **de uma vez**.

Fluxo:

```
Módulo A
Módulo B
Módulo C
Módulo D
      ↓
Integração completa
```

### Vantagem

* simples de implementar

### Desvantagem

* difícil identificar onde está o erro

---

## 4.2 Top-Down

A integração começa pelos **módulos de alto nível**.

Estrutura:

```
Interface
   ↓
Serviço
   ↓
Banco de dados
```

Quando módulos inferiores ainda não existem, usamos **stubs**.

### Stub

Um stub simula o comportamento de um módulo ainda não implementado.

Exemplo:

```python
def buscar_produto(id):
    return {"id": id, "nome": "Produto Teste", "preco": 10}
```

---

## 4.3 Bottom-Up

Começa pelos **módulos de baixo nível**.

Exemplo:

```
Banco de dados
   ↑
Serviços
   ↑
Interface
```

Nesse caso usamos **drivers** para simular módulos superiores.

---

## 4.4 Integração Incremental

Os módulos são integrados **gradualmente**.

Exemplo:

```
Módulo A + B
Módulo A + B + C
Módulo A + B + C + D
```

Essa é a estratégia **mais usada em desenvolvimento moderno**.

---

# 5. Exemplo Prático em Python

Sistema simples de biblioteca.

## Módulo 1 — Repositório de livros

```python
def buscar_livro(id):
    livros = {
        1: "Python Básico",
        2: "Algoritmos",
        3: "Estruturas de Dados"
    }
    return livros.get(id)
```

---

## Módulo 2 — Serviço de empréstimo

```python
def emprestar_livro(id):
    livro = buscar_livro(id)

    if livro is None:
        return "Livro não encontrado"

    return f"Livro '{livro}' emprestado"
```

---

## Teste de Integração

```python
def test_emprestimo():
    resultado = emprestar_livro(1)
    assert resultado == "Livro 'Python Básico' emprestado"
```

Aqui estamos testando:

* módulo de dados
* módulo de serviço

**juntos**.

---

# 6. Testando Integração com Banco de Dados

Exemplo simples usando SQLite.

```python
import sqlite3

def conectar():
    return sqlite3.connect("banco.db")

def buscar_usuario(id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT nome FROM usuarios WHERE id=?", (id,))
    resultado = cursor.fetchone()

    conn.close()

    return resultado
```

Teste de integração:

```python
def test_buscar_usuario():
    usuario = buscar_usuario(1)
    assert usuario is not None
```

Aqui estamos testando:

* código Python
* banco de dados
* consulta SQL

---

# 7. Integração com API

Outro cenário comum é integração com APIs.

Exemplo usando `requests`.

```python
import requests

def buscar_pokemon(nome):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome}"
    resposta = requests.get(url)
    return resposta.json()
```

Teste de integração:

```python
def test_buscar_pokemon():
    pokemon = buscar_pokemon("pikachu")
    assert pokemon["name"] == "pikachu"
```

---

# 8. Boas Práticas em Testes de Integração

1️⃣ Testar fluxos reais do sistema

2️⃣ Usar banco de dados de teste

3️⃣ Evitar dependência de serviços externos

4️⃣ Automatizar testes no CI/CD

5️⃣ Isolar ambientes de teste

