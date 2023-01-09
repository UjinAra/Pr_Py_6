# Напишите функцию print_operation_table(operation, num_rows=6, 
# num_columns=6), которая принимает в качестве аргумента функцию,
# вычисляющую элемент по номеру строки и столбца. Аргументы num_rows 
# и num_columns указывают число строк и столбцов таблицы, которые 
# должны быть распечатаны. Нумерация строк и столбцов идет с единицы 
# (подумайте, почему не с нуля). Примечание: бинарной операцией 
# называется любая операция, у которой ровно два аргумента, как, 
# например, у операции умножения.
# print_operation_table(lambda x, y: x * y)

import sys

#            print("{:>{}}".format(operation(row,column), colSize), end='\t')
#        print()

def dataInput(st):
    try:
      n = int(input(st)) # Число N
      if n==0:
        print("Вы ввели 0")
        sys.exit()  
    except ValueError:
        print("Вы ввели не число")
        sys.exit() 
    return n  

y1=int(dataInput("Введите число строк (Y)- "))
x1=int(dataInput("Введите число столбцов (X)- "))
func="lambda x, y: "+str(input("Введите выражение для функции c аргументами X и Y -"))

for i in range (y1+1):
    for j in range(x1+1):
        if i==0:
           print(j, end='\t') 
        elif j==0:
            print(i, end='\t') 
        else:
            print(eval(func)(i,j), end='\t')
    print()