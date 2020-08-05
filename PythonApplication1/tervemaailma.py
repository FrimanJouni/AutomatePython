
Tämä ohjelma sanoo terve ja kysyy nimeä ja ikää
print('Terve maailma')
print('Mikä on sinun nimi?') #Kysyy nimeä
munNimi = input()
print('Hauska tavata ' + munNimi)
print('Sun nimen pituus on :')
print(len(munNimi))
print('Kuinka vanha olet?') #Kysyy ikää
munIka = input()
print('Olet ' + str(int(munIka)+1) + 'vuotta vanha yhden vuoden kuluttua')

#for i in range(60):
#    testi = i - 1 % 60
#    print(testi)