# Vegyük elő azt a programunkat, amelyik a felhasználó nevét és korát kezeli. 
# A felhasználó-nak javasoljunk életkorának megfelelő olvasnivalót!
# a.0–3 év: „Totyogóknak a kettes számrendszerről”
# b.4–6 év: „Hackeljük meg az óvodát!”
# c.7–14 év: „Felhőtechnológia a menzán”
# d.15–18 év: „Big data a középiskolában"
nev=input("Írd be aneved: ")
kor= int( input("Írd be a korod: "))
if kor>=0 and kor<=3:
    print("Kedves", nev, "! Neked a 'Totyogóknak a kettes számrendszerről' címet ajánlom!")
elif kor>=4 and kor<=6:
    print("Kedves", nev, "! Neked a 'Hackeljük meg az óvodát!' címet ajánlom!")
elif kor>=7 and kor<=14:
    print("Kedves", nev, "! Neked a 'Felhőtechnológia a menzán' címet ajánlom!")
elif kor>=15 and kor<=18:
    print("Kedves", nev, "! Neked a 'Big data a középiskolában' címet ajánlom!")
else:
    print("Számodra nincs ajánlat!")

