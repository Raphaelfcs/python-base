#!/usr/local/bin/python

"""
Relatório de alunos por atividade
Imprimir a lista de alunos agrupadas por sala
que frequenta cada umas das atividades
"""

__version__ = "0.1.0"
__author__ = "Raphael Santos"
__license__ = "Unlicese"

sala1 = ["Erick", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["João", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erick", "Maia","Joana","Carlos", "Antonio"]
aula_musica = ["Erick","Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
    ("Inglês", aula_ingles), 
    ("Música", aula_musica),
    ("Dança", aula_danca)
    ]
# Listar aluns em cada atividade por sala

for nome_atividade, atividade in atividades:

    print(f"Alunos da atividade {nome_atividade}\n")
    print("-"* 40)
    # SALA 1 quem tem interseção com a atividade em questão

    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2).intersection(atividade)
            
    print("sala 1: ",atividade_sala1)
    print("sala 2: ",atividade_sala2)

    print()
    print("#" * 40)