import random
from time import perf_counter

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
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


correct_answers_index = [1, 2, 0, 3, 1]


def esCorrecto (resp,correcta):
    if resp == correcta:
        return True
    else:
        return False


def esNum (num):
    if num.isdigit():
        return True
    else:
        return False

#variable que guarda todas las preguntas con sus respuestas y con el indice de la respuesta correcta
questions_to_ask = random.choices(list(zip(questions,answers, correct_answers_index)), k=3) 
         
puntaje = 0.0
bien = 1
mal = 0.5    
error = 0

for pregunta, respuestas, respuesta_index in questions_to_ask:
    print(pregunta)
    for i, respuesta in enumerate(respuestas):
        print(f'{i+1}-{respuesta}')
    for i in range(2):
        user_answer = input("Respuesta: ")
        if esNum(user_answer):
            user_answer = int(user_answer)
            user_answer -= 1
            if esCorrecto(user_answer,respuesta_index):
              print("¡Correcto!")
              puntaje = puntaje + bien
              break
            else:
              error += 1
              if error == 2:
                print("Incorrecto. La respuesta correcta es:")               
                print(respuesta_index)
                exit(1)
              else: 
                  print("Respuesta incorrecta")
            puntaje = puntaje - mal
        else:
           print("ERROR FATAL! POR FAVOR! INGRESE UN NUMERO VALIDO!!!!")
           exit(1)
     # Se imprime un blanco al final de la pregunta
    print()
print(f"Tu puntaje fue de {puntaje} puntos")