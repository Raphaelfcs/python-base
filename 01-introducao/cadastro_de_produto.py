#!/usr/local/bin/python

"""
Cadastro de Produto
"""

__version__ = "0.1.0"
__author__ = "Raphael Santos"
__license__ = "Unlicese"

import pprint

produto = {
"nome" : "Caneta",
"cores" : ["azul", "branco"],
"preco" : 3.23,
"dimensao" :{
    "altura" : 12.1,
    "argura" : 0.8,
},
"em_estoque" : True,
"codigo" : 45678,
"codbar" : None,
}


cliente = {
    "nome" : "Raphael"
}

compra = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": 3
}

#pprint.pprint(compra)

total_compra = compra["quantidade"] * compra['produto']["preco"]

print(
    f"O cliente {compra['cliente']['nome']}"
    f" comrpou {compra['quantidade']} unidades de {compra['produto']['nome']} de cor {compra['produto']['cores'][1]}"
    f" e pagou o total da {total_compra}"
)