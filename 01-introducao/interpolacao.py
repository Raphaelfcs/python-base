#!/usr/local/bin/python
"""Cria uma mensagem de spam 
    Pode ser usado para itens procmocionais
    sendo assim substitua as labes por coisas eficientes
"""
__version__ = "0.1.0"
__author__ = "Raphael"


email_tmpl = """
 Olá, %(nome)s
 Tem inetresse em comprar %(produto)s?
 
 Este produto é otimo para resolver
 %(texto)s 
 
 Clique agora em %(link)s
 
 Apneas %(quantidade)d disponíveis!
 
 Preço promocional %(preco).2f
 
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
        },"\N{party popper}")