# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

osnovanie = int(input("Введите основание числа, степень которого нужно найти: "))
stepen = int(input("Введите степень, в которую необходимо возвести число: "))

def our_function(osnovanie, stepen):
  if stepen == 1:
    return osnovanie
  else:
    return osnovanie * our_function(osnovanie, stepen - 1)
print(f"Число {osnovanie} в степени {stepen} равно: {our_function(osnovanie, stepen)}")