#Conwayn Game of Life

import random, time, copy
WIDTH = 60
HEIGHT = 20
sSolut=[] #Luodaan lista soluille ja täytetään se elävillä ja kuolleilla soluilla 
for x in range(WIDTH):
    sarake = []
    for y in range(HEIGHT):
        if random.randint(0,1) == 0: #Glider patternin saa jos kiinnostaa nähdä tunnistettuja muotoja pelissä (x, y) in ((1, 0), (2, 1), (0, 2), (1, 2), (2, 2)):
            sarake.append('#') #Lisätään elävä solu
        else:
            sarake.append(' ') #Kuollut solu
    sSolut.append(sarake) #sSolut on lista täynnä sarake listoja

while True:
    print('\n\n\n\n\n') #Tulostetaan rivinvaihtoja jotta solujen liikkuminen näkyy selvästi
    nSolut = copy.deepcopy(sSolut)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(nSolut[x][y], end='') #Tulostetaan joko # tai tyhjä väli, elävä tai kuollut solu
        print() #Rivinvaihto rivin lopussa
    for x in range(WIDTH):
        for y in range(HEIGHT): #Saadaan naapureiden koordinaatit, "% WITDH varmistaa että pysytään aina koordinaatistossa
            vasenKoordi = (x-1) % WIDTH
            oikeaKoordi = (x+1) % WIDTH
            ylaKoordi = (y-1) % HEIGHT
            alaKoordi = (y+1) % HEIGHT
            naapurit = 0 #Naapurien määrä
            if nSolut[vasenKoordi][ylaKoordi]=='#': #Tarkastetaan kaikkien ympärillä olevien solujen "elo" ja lisätään naapurien määrän laskuria
                naapurit += 1
            if nSolut[x][ylaKoordi]=='#': #Kyseisen solun vasen yläpuoli tarkastetaan, jos hengissä eli # niin lisätään naapurilukua
                naapurit += 1
            if nSolut[oikeaKoordi][ylaKoordi]=='#':
                naapurit += 1
            if nSolut[vasenKoordi][y]=='#':
                naapurit += 1
            if nSolut[oikeaKoordi][y]=='#':
                naapurit += 1
            if nSolut[vasenKoordi][alaKoordi]=='#':
                naapurit += 1
            if nSolut[x][alaKoordi]=='#':
                naapurit += 1
            if nSolut[oikeaKoordi][alaKoordi]=='#':
                naapurit += 1
            if nSolut[x][y]=='#' and (naapurit==2 or naapurit == 3): #Pelin säännöt, jos elävällä 2tai3 naapuria se pysyy hengissä
                sSolut[x][y] = '#'
            elif nSolut[x][y] == ' ' and naapurit==3: #Jos kuolleella tasan 3 naapuria herää henkiin
                sSolut[x][y] = '#'
            else:                       #Kaikissa muissa tapauksissa kuolee.
                sSolut[x][y]=' '
    time.sleep(1) #Ettei tulosteta ihan kauheaa vauhtia