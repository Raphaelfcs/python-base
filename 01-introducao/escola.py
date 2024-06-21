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
atividades = [aula_ingles, aula_musica, aula_danca]
# Listar aluns em cada atividade por sala

aula_ingles_sala1 = []
aula_ingles_sala2 = []

for aluno in aula_ingles:
    if aluno in sala1:
        aula_ingles_sala1.append(aluno)
    elif aluno in sala2:
        aula_ingles_sala2.append(aluno)


aula_musica_sala1 = []
aula_musica_sala2 = []

for aluno in aula_musica:
    if aluno in sala1:
        aula_musica_sala1.append(aluno)
    elif aluno in sala2:
        aula_musica_sala2.append(aluno)


print("Atividades sala 1: ","Musica" ,aula_musica_sala1, "Ingles", aula_ingles_sala1)
print("Atividades sala 2: ","Musica" ,aula_musica_sala2, "Ingles", aula_ingles_sala2)