#Maaginen ennustava 8-pallo joka myös näyttää ensimmäiset def functions.

import random
def haeVastaus(vastausNro): #Määritellään funktio
    if vastausNro == 1: #Esim. ehtolauseilla sisältö
        return 'Se on varmaa'
    elif vastausNro == 2:
        return 'Vahva ehkä'
    elif vastausNro == 3:
        return 'Ei toivoa'
    elif vastausNro == 4:
        return 'En luottaisi'   #Returneilla palautusarvon määrittely
    elif vastausNro == 5:
        return 'Lotto vetämään'
    else:
        return 'Pullalla ne sorsatkin elää'

r = random.randint(1,6)
ennustus = haeVastaus(r) #Kutsutaan funktiota argumenttina satunnainen numero
print(ennustus)
