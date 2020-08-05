#Try ja Except virheen käsittelyä

def virheenK(jaetaan):
    try:
        return 42 / jaetaan
    except ZeroDivisionError:
        print('Virhe, väärä inputti')
print(virheenK(2))
print(virheenK(12))
print(virheenK(0))
print(virheenK(4))

#Toimii myös jos funktion kutsu laitetaan try-except blokin sisään

def virheenK(jaetaan):
    return 42 / jaetaan
try:
    print(virheenK(2))
    print(virheenK(12))
    print(virheenK(0))
    print(virheenK(4)) #Tätä kutsua ei tosin tässä tapauksessa käsitellä, sillä try komento siirtyy eteenpäin exceptiin virheen havaitessaan.
except ZeroDivisionError:
    print('Virhe, väärä inputti')
