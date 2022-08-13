from array import array
from fileinput import filename
from itertools import permutations
from multiprocessing.dummy import Array
from pickle import TRUE

class THajo:
    def __init__(self, boldal, joldal, balNevek, jobbNevek):
        self.balOldal=boldal
        self.jobbOldal=joldal
        self.Balkezesek= balNevek
        self.Jobbkezesek=jobbNevek
        
    def hosszanti_nyomatek_oldal(self, permut, evezosok):
        nyomatek=0.0
        tav=[0.675/2+4*0.675, 0.675/2+3*0.675, 0.675/2+2*0.675, 0.675/2+0.675, 0.675/2, -0.675/2, -0.675/2-0.675, -0.675/2-2*0.675, -0.675/2-3*0.675, -0.675/2-4*0.675]
        for i in range(len(permut)):
            s=evezosok[i].suly
            t=tav[permut[i]] 
            nyomatek+=s*t
        return nyomatek

    def hosszantiOssznyomatek(self):
        return self.hosszanti_nyomatek_oldal(self.jobbOldal, self.Jobbkezesek) +  self.hosszanti_nyomatek_oldal(self.balOldal, self.Balkezesek)

    def kiiras(self):
        b=['-','-','-','-','-','-','-','-','-','-']
        j=['-','-','-','-','-','-','-','-','-','-']
        for i in range(len(self.Balkezesek)):
            b[self.balOldal[i]]=self.Balkezesek[i].nev
        for i in range(len(self.Jobbkezesek)):
            j[self.jobbOldal[i]]=self.Jobbkezesek[i].nev
        for i in range(10):
            print(f"{i+1}.sor\t {b[i]}\t\t\t\t{j[i]}")
        # print(j)
        # print(b)

class Tadat:
    def __init__(self, sor):
        elem=sor.strip().split(';')
        self.nev=elem[0]
        self.suly=int(elem[1])
        self.kezes=elem[2]
        self.poz=int(elem[3])
    
    def kiir(self):
        print(self.nev, self.suly, self.kezes, self.poz)

def hosszanti_legjobbak(balos, jobbos):
    hajok=[]
    balosPoz=list( permutations(range(10), len(balos)))
    jobbPoz=list( permutations(range(10), len(jobbos)))
    balosPoz=felesleg_eltavolitasa(balosPoz, balos)
    jobbPoz=felesleg_eltavolitasa(jobbPoz, jobbos)
    minMom=999999999999
    minB=0
    minJ=0
    for i in range(len(balosPoz)):
        for j in range(len(jobbPoz)):
            bmom=hosszantiNy1oldal(balosPoz[i],balos)
            jmom=hosszantiNy1oldal(jobbPoz[j], jobbos)
            mom=bmom+jmom
            if abs(minMom) >= abs(mom) and minB != i and minJ!=j: 
                minMom = mom
                minB=i
                minJ=j
                print("Min=", minMom, balosPoz[minB], jobbPoz[minJ])
                hajok.append(THajo( balosPoz[minB], jobbPoz[minJ],  balos, jobbos))
    return hajok



def felesleg_eltavolitasa(Poz, oldal):
    P=[]
    j=len(Poz)-1        # végéről indít
    while j>=0:
        kidob=False
        poziciok=Poz[j]
        for i in range( len(oldal)): # minden evezős
            a=poziciok[i]
            b=oldal[i].poz
            if a!=b and b!=-1:
                kidob=True
                break
        
        if(not kidob):       
            P.append(poziciok)
            
        j-=1
    return P

def beolvas(fileName):
    f = open(fileName, "r", encoding="utf-8")
    sor=f.readline().strip()
    for sor in f:
        a=Tadat(sor)
        if a.kezes=="B":
            balos.append(a)
        elif a.kezes=="J":
            jobbos.append(a)
        else:
            mindegy.append(a)

def hosszantiNy1oldal( permut, evezosok):
        nyomatek=0.0
        tav=[0.675/2+4*0.675, 0.675/2+3*0.675, 0.675/2+2*0.675, 0.675/2+0.675, 0.675/2, -0.675/2, -0.675/2-0.675, -0.675/2-2*0.675, -0.675/2-3*0.675, -0.675/2-4*0.675]
        for i in range(len(permut)):
            s=evezosok[i].suly
            t=tav[permut[i]] 
            nyomatek+=s*t
        return nyomatek  

def ki_hol_uljon(balos, jobbos, mindegy):
    b=balos
    j=jobbos
    m=mindegy
    jo_ulésrend=[]
    for i in range( 1,len(mindegy)):
        balra=permutations(mindegy, i)
        b.extend(balra)
        print(balra)
        print(b)


    return b


    
    
#főprogram 
if __name__ == "__main__":
    balos=[]
    jobbos=[]
    mindegy=[]
    hajok=[]
    fileName="evezosok.txt"
    beolvas(fileName)

    #jo_ulésrend=ki_hol_uljon(balos, jobbos, mindegy)

    hajok=hosszanti_legjobbak(balos, jobbos)
    hajok.reverse()
    for i in range(3):
        print(f"{i}. hajó hosszanti momentum: {hajok[i].hosszantiOssznyomatek()}")
        hajok[i].kiiras()
        print()
    
    print("End")
