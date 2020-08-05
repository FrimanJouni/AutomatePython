#Arvataan numero 1-20

import random
salaNum = random.randint(1,20)
print('Ajattelen numeroa väliltä 1-20')
for arvauksetNro in range(1,6):
    print('Arvaa mitä numeroa ajattelen?')
    arvaus = int(input())
    if arvaus < salaNum:
        print('Liian pieni')
    elif arvaus > salaNum:
        print('Liian suuri')
    else:
        break #Oikea vastaus

if arvaus == salaNum:
    print('Hyvää työtä, arvasit oikein ' + str(arvauksetNro) + '. arvauksellasi')
else:
    print('Väärin meni, ajattelin numeroa ' + str(salaNum))