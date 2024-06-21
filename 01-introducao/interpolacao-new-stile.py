#!/usr/local/bin/python
"""Cria uma mensagem de spam 
    Pode ser usado para itens procmocionais
    sendo assim substitua as labes por coisas eficientes
"""
__version__ = "0.1.0"
__author__ = "Raphael"


email_tmpl = """
 Olá, {nome}
 Tem inetresse em comprar {produto}?
 
 Este produto é otimo para resolver
 {texto}. 
 
 Clique agora em {link}
 
 Apneas {quantidade} disponíveis!
 
 Preço promocional {preco}
 
 """

clientes = ["Raphael", "Steicy", "Izabela"]

for cliente in clientes:
    print(
        email_tmpl
        % {
            "nome": cliente,
            "produto": "caneta",
            "texto": "Escrever muito bem",
            "link" : "https://canetaslegais.com",
            "quantidade": 1, "preco": 50.5
        })
    print("\U0001f43C")