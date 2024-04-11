#Difrencias entre el tiempo de los cursos
cursos_mini = 2.5
cursos_medio = 4
cursos_max = 7
dalto_curso = 1.5

#Crudo de promedio
crudo_promedio = 5
crudo_dalto = 1.5

#Promedio de porcentaje entre los demas cursos.
diferencia_con_min = 100 - dalto_curso / cursos_mini * 100
diferencia_con_medio = 100 - dalto_curso / cursos_medio * 100
diferencia_con_max = 100 - dalto_curso * 1000 // cursos_max / 10
print('----------------')

#Imprimir resultado
print(f' el curso de dalto duro un {diferencia_con_min} por ciento menos que el minimo')
print(f' el curso de dalto duro un {diferencia_con_medio} por ciento menos que el medio')
print(f' el curso de dalto duro un {diferencia_con_max} por ciento menos que el maximo')
print('----------------')
#Calculando el porcentaje de tiempo vacio removido
tiempo_vacio_promedio = 100 - cursos_medio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 10

#Mostrando los vacios que se remueven
print(f'Un curso promedio elimina {tiempo_vacio_promedio}% de tiempo vacio')
print(f'Este curso elimino el {tiempo_vacio_dalto}% del tiempo vacio')
print('----------------')

#Mostrando diferencias de horas con otros cursos
print(f'Ver 10 horas del curso de dalto equivale a ver {cursos_medio * 1000 // dalto_curso / 100} horas de otros cursos')
print(f'Ver 10 horas del curso de dalto equivale a ver {dalto_curso * 100 // cursos_medio / 10} horas de este curso')
print('----------------')
