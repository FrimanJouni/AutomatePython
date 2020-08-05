
#Tarkistaa salasanan oikeaksi
nimi = input()
salasana = input()
if nimi == 'Jone': #Nimen pitää olla oikein muuten ei edes tarkista salasanaa, HUOM myös kaksoispiste
    print('Terve ' + nimi)
    if salasana=='miekkakala':
        print('Salasana oikein')
    elif salasana=='kuukupööpö':    # if / elif / else HUOM sisennykset
        print('Pakko ottaa')
    else:
        print('Salasana väärin')

#Ei myöskään anna mitään prompteja käyttäjälle, ihan vitun leethaxor