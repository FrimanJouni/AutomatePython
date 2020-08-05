# Uusien moduulien lisääminen

import random #satunnainen numero 5 kertaa
import sys #systeemikirjasto

for i in range(5):
    print(random.randint(1,10))


while True:
    print('Kirjoita poistu poistuaksesi ohjelmasta')
    vastaus = input()
    if vastaus == 'poistu':
        sys.exit()
    print('Kirjoitit ' + vastaus + ' lol tyhmä')