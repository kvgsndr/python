


class Tadat:
    def __init__(self, elem):
        self.nev=elem[0]
        self.suly=int(elem[1])
        self.kezes=elem[2]
    
    def kiir(self):
        print(self.nev, self.suly, self.kezes)


def beolvas(fileName):
    f = open(fileName, "r", encoding="utf-8")
    sor=f.readline().strip()
    for sor in f:
        elemek=sor.strip().split(';')
        a=Tadat( elemek )
        if a.kezes=="B":
            balos.append(a)
        elif a.kezes=="J":
            jobbos.append(a)
        else:
            mindegy.append(a)
    
def perm_kiir(permut):
    for elem in permut:
        nyomatek=0.0
        for e in elem:
            e.kiir()
        print()

def oldal_kiir(lista):
    for i in lista:
        i.kiir()
    

def oldal_moment(adottPermut):
    nyomatek=0.0
    for e in adottPermut:
        nyomatek+=e.suly*0.3
    return nyomatek

def hossz_moment(adottPermut):
    nyomatek=0.0
    tav=[0.675/2+4*0.675, 0.675/2+3*0.675, 0.675/2+2*0.675, 0.675/2+0.675, 0.675/2, -0.675/2, -0.675/2-0.675, -0.675/2-2*0.675, -0.675/2-3*0.675, -0.675/2-4*0.675]
    for i in range(len(adottPermut)):
        nyomatek+=adottPermut[i].suly*tav[i]
    return nyomatek

def bovit():
    senki=Tadat("senki;0;B".strip().split(';')) 
    for i in range(20-len(balos)):
        balos.append(senki)

    senki=Tadat("senki;0;J".strip().split(';'))
    for i in range(20-len(jobbos)):
        jobbos.append(senki)



    

if __name__ == "__main__":
    fileName="evezosok.txt"
    balos=[]
    jobbos=[]
    mindegy=[]
    beolvas(fileName)
    bovit()
    Jpermut=permutations(jobbos)
    Bpermut=permutations(balos)
    #perm_kiir(Bpermut)
    #perm_kiir(Jpermut)
    listBpermut=list(Bpermut)
    listJpermut=list(Jpermut)
    
    a=oldal_moment(listJpermut[0])
    print("oldal a=", a)
    b=oldal_moment(listBpermut[0])
    print("oldal b=", b)
    moment=b-a
    print("oldal MOMENT", moment)
    min_moment=100000000.0
    for i in range(len(listBpermut)):
        for j in range(len(listJpermut)):
            a=hossz_moment(listBpermut[i])
            #oldal_kiir(listBpermut[i])
            #print("Hossz a=", a)
            b=hossz_moment(listJpermut[j])
            #oldal_kiir(listJpermut[i])
            #print("hossz b=", b)
            moment=b+a
            print("MOMENT", moment, i,j)
            if min_moment>moment:
                mini=i
                minj=j
                min_moment=moment

    print("Minimalis momen hoszanti= ", min_moment)
    oldal_kiir(listBpermut[mini])
    oldal_kiir(listJpermut[minj])
