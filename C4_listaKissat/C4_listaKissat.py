#Listan käytön opettelua

kissaNimet = [] #Tyhjän listan luominen
while True:
    print('Anna kissan ' + str(len(kissaNimet) + 1) + '. nimi tai kirjoita quit lopettaaksesi') #Tulostaa numerojärjestyksen nimien annolle.
    nimi = input()
    if nimi == 'quit':
        break
    elif nimi in kissaNimet: #in-not in, tarkistaa onko nimi jo listalla
        print('Nimi on jo kirjattu')
    else:
        kissaNimet = kissaNimet + [nimi]

print('Kissojen nimet ovat : ')
for ovelasekoittamatonmuuttuja in kissaNimet: #Tässä voisi käyttää typerän muuttujanimen sijaan nimi-muuttujaa, mutta se ei siis ole sama muuttuja kuin edellä olevassa inputista saatu. HUOM scope
    print(' ' + ovelasekoittamatonmuuttuja)

#Listojen muistipaikka/referenssi.

def referenssiLista(parametri):
    parametri.append('Lista ei käytä muistireferenssiä vaan muuttaa suoraan listaa itsessään') #Listaa muutetaan metodi-funktiolla ja muutos säilyy myös funktion lakattua.

lista = ['Stringit', 'käyttävät', 'muistireferenssejä joten niitä ei voi muuttaa itsessään. ']

referenssiLista(lista)
print(lista)