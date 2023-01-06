# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько
# легко он их придумывает, Вам стоит написать программу. Винни-Пух 
# считает, что ритм есть, если число слогов (т.е. число гласных букв) 
# в каждой фразе стихотворения одинаковое. Фраза может состоять из
# одного слова, если во фразе несколько слов, то они разделяются 
# дефисами. Фразы отделяются друг от друга пробелами. Стихотворение 
# Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам 
# пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом 
# все не в порядке

def ritmTF(st):
    ritm=False
    sogl=["к","п","с","т","ф","х","ц","ч","ш","щ","б","в","г","д","ж","з","й","л","м","н","р","ь","ъ"]
    glas=["а","у","о","и","э","ы","я","ю","е","ё"]
    countG=0
    countSog=0
    for i in range(len(st)):
        if st[i] in sogl:
            countSog =countSog + 1
        if st[i] in glas:
            countG=countG+1
    if countG==countSog:
        ritm=True          
    return ritm 

stih=input("Введите стихотворение винипуха, слова разделяются тире, а фразы пробелом - ").split()
for i in range(len(stih)):
    ritmVP=ritmTF(stih[i])
    
if ritmVP == True:
    print ("Парам пам-пам")
else:
    print("Пам парам")
    
    