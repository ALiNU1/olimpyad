'''
Пицца – любимое лакомство Васи, он постоянно покупает и с 
удовольствием употребляет различные сорта этого великолепного блюда. 
Однажды, в очередной раз, разрезая круглую пиццу на несколько частей, Вася задумался: на какое 
максимальное количество частей можно разрезать пиццу за N прямых разрезов?
Помогите Васе решить эту задачу, определив максимальное число не обязательно равных кусков, 
которые может получить Вася, разрезая пиццу таким образом.
'''

# n = int(input())
# print(int(n*(n+1)/2)+1)

'''
В доме Вилли установили скоростной лифт новой экспериментальной модели. 
В этом лифте кнопки с номерами этажей заменены двумя другими кнопками. 
При нажатии на первую кнопку лифт поднимается на один этаж вверх, 
а при нажатии на вторую – опускается на один этаж вниз.
Младшему брату Вилли Дилли очень нравится кататься на новом лифте. 
Он катается на нём до тех пор, пока не побывает на каждом из этажей хотя бы по одному разу. 
После этого Дилли довольный возвращается домой.
Зная порядок, в котором Дилли нажимал на кнопки лифта, попробуйте определить 
общее количество этажей в доме Вилли и Дилли.
'''

# x = input()
# maxE = 0
# minE = 0
# T = 0
# for i in range(len(x)):
#     if x[i] == '1':
#         T+=1
#     else:
#         T-=1
#     if maxE<T:
#         maxE = T
#     elif minE>T:
#         minE = T
# print(abs(minE)+abs(maxE)+1)

'''
Задано натуральное число n. Необходимо перевести его в k-ичную систему счисления и найти разность между произведением 
и суммой его цифр в этой системе счисления.
Например, пусть n = 239, k = 8. Тогда представление числа n в восьмеричной системе 
счисления — 357, а ответ на задачу равен 3 × 5 × 7 − (3 + 5 + 7) = 90.
'''

# a,b = map(int,input().split())
# def per(a,b):
#     res = a%b
#     a = a//b
#     mn = 10
#     while a>0:
#         res = res+((a%b)*mn)
#         mn*=10
#         a=a//b
#     return res 
# def otvet(a):
#     s=0
#     p=1
#     while a>0:
#         x=a%10
#         a = a//10
#         s+=x
#         p*=x
#     return p-s
# print(otvet(per(a,b)))

'''
Необходимо вычислить значение 2n.
'''

# n = int(input())
# print(2**n)

'''
Задана последовательность, состоящая только из символов ‘>’, ‘<’ и ‘-‘. Требуется найти количество стрел, 
которые спрятаны в этой последовательности. Стрелы – это подстроки вида ‘>>-->’ и ‘<--<<’.
'''

# import sys
# try:
#     a = input()
# except EOFError:
#     print(0)
#     sys.exit()
# res = 0
# for i in range(4,len(a)):
#     if (a[i-4:i+1]) == '>>-->' or a[i-4:i+1] == '<--<<':
#         res +=1
# print(res)

'''
Требуется найти разность между неотрицательными числами А и В.
'''

# a = int(input())
# b = int(input())
# print(a-b)