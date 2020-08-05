#Collatzin sekvenssi joka palauttaa aina lopulta numeron 1, kun sille annetaan mikä tahansa kokonaisluvun

def collatz(luku):
    lukuO = luku
    luku = luku % 2
    if luku == 0:
        return lukuO // 2
    if luku == 1:
        return lukuO * 3 + 1


print('Anna luku')
inputti = input()

while inputti != 1:
    inputti = collatz(int(inputti))
    print(inputti)


