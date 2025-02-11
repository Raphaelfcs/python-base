#!/usr/local/bin/python

"""
Hello World Multi Linguas.

Dependendo da lingua configurada no ambitente o programa exibe a mensagem 
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

  export LANG=pt_BR

Execução:
  
  python3 hello.py
  ou
  ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Raphael Santos"
__license__ = "Unlicese"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = {

     "pt_BR" : "Olá, Mundo!",
     "it_IT" : "Ciao, Mondo!",
     "en_US": "Hello, World!",
     "fr_FR" : "Bonjour, Monde!",
     "es_SP": "Hola, Mundo!"
}

print(msg[current_language],"\U0001f43C")