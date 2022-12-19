# №1. Напишите программу, которая принимает на вход 5 чисел и 
# находит максимальное из них.

num_max=0
for i in range (5):
    num = int(input("Введите число: "))
    if num_max<num:
        num_max=num
print(num_max)