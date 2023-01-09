#Напишите функцию same_by(characteristic, objects), которая проверяет, 
# все ли объекты имеют одинаковое значение некоторой характеристики, 
# и возвращают True, если это так. Если значение характеристики для 
# разных объектов отличается - то False. Для пустого набора объектов, 
# функция должна возвращать True. Аргумент characteristic - это функция,
# которая принимает объект и вычисляет его характеристику.
#Пример:
#same_by(lambda x: x % 2, [2,4,6,8])
#Ответ: True

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

spList = list(map(int, input("Задайте последовательность чисел через пробел:").split()))
func="lambda x:"+str(input("Введите выражение для функции c аргументами X - "))
print(spList)
print(func)
print(all(eval(func) for x in [spList]))