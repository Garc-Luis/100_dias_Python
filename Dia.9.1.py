student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Crear un diccionario vacío llamado student_grades.
student_grades = dict()

# TODO-2: Escriba su código a continuación para agregar las calificaciones a student_grades.👇
for k in student_scores:
    score = student_scores[k]
    if score < 70:
        student_grades[k] = "Fail"
    elif score > 70 and score < 80:
        student_grades[k] = "Acceptable"
    elif score > 80 and score < 90:
        student_grades[k] = "Exceeds Expectations"
    elif score > 90:
        student_grades[k] = "Outstanding"

# 🚨 Don't change the code below 👇
print(student_grades)