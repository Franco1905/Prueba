# -*- coding: utf-8 -*-

import random
# Preguntas para el juego
questions = [
"¿Qué función se usa para obtener la longitud de una cadena en Python?",
"¿Cuál de las siguientes opciones es un número entero enPython?",
"¿Cómo se solicita entrada del usuario en Python?",
"¿Cuál de las siguientes expresiones es un comentario válido en Python?",
"¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
("size()", "len()", "length()", "count()"),
("3.14", "'42'", "10", "True"),
("input()", "scan()", "read()", "ask()"),
(
"// Esto es un comentario",
"/* Esto es un comentario */",
"-- Esto es un comentario",
"# Esto es un comentario",
),
("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
ans = 0
ind = 0
for i in range(len(questions)):
    print(f"Pregunta numero {i + 1}: {questions[i]} ")
    for z in range(len(answers[i])): 
        print (f"{z+1}) {answers[i][z]}")
    ans = int(input("Inserte su respuesta: "))
    if ans == correct_answers_index[i]:
        print("Respuesta correcta!!")
    else:
        print("Respuesta incorrecta!")
    
