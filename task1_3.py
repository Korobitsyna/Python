# Напишите программу, которая на вход будет принимать
# число N и выыводить числа от -N до +N

num = int(input("Введите число: "))
print(list(range(-num,num+1)))
