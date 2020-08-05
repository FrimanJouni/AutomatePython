#Yhteenlaskua

total = 0
for num in range(101): #100 kertaa lisää järjestysnumeron totaliin. HUOM käytetty eri muuttujaa
    total = total + num
    print(total)
print(total)

for i in range(12, 26): #kahdella annetaan lähtö- ja lopetusarvot, lopetusarvoa ei lasketaan mukaan vaan sitä edellinen luku on viimeinen luettu arvo
    print(i)


for i in range(0,12,2): #kolmella annetaan lähtö- ja lopetusarvojen lisäksi askeleet kuinka monella arvo lisääntyy jokaisella kierroksella
    print(i)


for j in range(5,-1, -1): #Myös negatiivinen askellus onnistuu
    print(j)

#Tämä onnistuisi myös esimerkiksi taulukoilla, tässä aiheuttaisi errorin koska ei määritelty taulukkoNimiä

for nimi in taulukkoNimiä:
    print(nimi)
