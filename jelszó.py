# Kérjünk be jelszót a felhasználótól, 
# és hasonlítsuk össze a programban tárolttal! 
# Ha a fel-használó eltalálta a jelszót, írjuk ki, 
# hogy „Helyes jelszó.”, különben „Hozzáférés megtagadva.”.

jelszo='Admin1234'
beirt_jelszo = input('Írd be a jelszavad: ')
if jelszo == beirt_jelszo:
    print("Helyes jelszó.")
else:
    print("Hozzáférés megtagadva.")