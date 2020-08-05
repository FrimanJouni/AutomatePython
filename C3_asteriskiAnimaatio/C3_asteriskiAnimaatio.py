#Pieni loppumaton animaation asteriskilla

import time, sys
rako = 0 #alussa oleva väli ennen asteriskia joka rivillä
rakoKasvaa = True
try:
    while True: #Päälooppi joka jatkuu loputtomasti
        print(' ' * rako, end='') #printataan väli ennen asteriskeja rako muuttajan verran + lopusta otetaan rivinvaihto pois
        print('**********')
        time.sleep(0.1) #Pausettaa 0.1 sekuntia
        if rakoKasvaa:
            rako += 1
            if rako == 20:
                rakoKasvaa = False #rakoKasvaa vaihtuu Boolean tilojen välillä 0-20 saavutettuaan ja vaihtaa if-lauseesta toiseen
        else:
            rako -= 1
            if rako == 0:
                rakoKasvaa = True
except KeyboadInterrupt:
    sys.exit()
