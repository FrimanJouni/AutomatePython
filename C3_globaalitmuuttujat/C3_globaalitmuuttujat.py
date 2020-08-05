#Muutamia keissejä siitä miten globaalit muuttujat toimivat, ei mitään tiettyä ohjelmaa

eggs = 'funktio käyttää globaalia muuttujaa'
def spam():
    print(eggs)
spam()

def possu(): #global statement funktion sisällä muuttaa globaalia muuttujaa vaikka scope on local funktiossa
    global pihvi
    pihvi = 'nautaa'
pihvi = 'possua'
possu()
print(pihvi)