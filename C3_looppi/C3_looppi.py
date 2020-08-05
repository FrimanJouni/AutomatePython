#tyhymä ohjelma looppi ärsytys, niin kauan kunnes vastaa nimesi jatkaa kirjoita nimesi kysymistä
nimi = ''
laskuri = 0
while nimi !='nimesi':
    print('Kirjoita nimesi')
    laskuri += 1
    nimi = input()
    if laskuri >= 3: #lisätty break laskuri että vain kolmeyritystä jäljellä ettei looppi pyöri loputtomasti huumorintajuttomilla
        print('nyt loppu yritykset')
        break
print('Kiitos')
