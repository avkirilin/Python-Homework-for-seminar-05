# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
# 4
import random
num_one = int(random.randint(0, 100))
print(f"Первое число = {num_one}")
num_two = int(random.randint(0, 100))
print(f"Второе число = {num_two}")


def sum_num(num):
    if num == 1:
        return 1
    else:
        return 1 + sum_num(num - 1)


print(f"{num_one} + {num_two} = {sum_num(num_one) + sum_num(num_two)}")
