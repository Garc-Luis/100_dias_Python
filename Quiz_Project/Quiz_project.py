from Question_model import  Question
from Quiz_data import question_data


banco_preguntas = list()
for i in question_data:
    pregunta_texto = i['text']
    pregunta_respuesta = i['answer']
    nueva_pregunta = Question(pregunta_texto, pregunta_respuesta)
    banco_preguntas.append(nueva_pregunta)


print(banco_preguntas)