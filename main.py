import math
print("Введите стороны треугольника")
print("Сторона A = ")
a = int(input())
print("Сторона B = ")
b = int(input())
print("Сторона C = ")
c = int(input())
if a<b+c and b<a+c and c<a+b :
    p = (a+b+c)/2
    s = str(round(math.sqrt(p*(p-a)*(p-b)*(p-c))))
    print('Площадь треугольника = '+s)
else : print("Такого треугольника не существует")