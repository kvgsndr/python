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
        
    def hosszantiNyomatek(self, permut, evezosok):
        nyomatek=0.0
        tav=[0.675/2+4*0.675, 0.675/2+3*0.675, 0.675/2+2*0.675, 0.675/2+0.675, 0.675/2, -0.675/2, -0.675/2-0.675, -0.675/2-2*0.675, -0.675/2-3*0.675, -0.675/2-4*0.675]
        for i in range(len(permut)):
            s=evezosok[i].suly
            t=tav[permut[i]] 
            nyomatek+=s*t
        return nyomatek

    def hosszantiOssznyomatek(self):
        return self.hosszantiNyomatek(self.jobbOldal, self.Jobbkezesek) -  self.hosszantiNyomatek(self.balOldal, self.Balkezesek)

    def kiiras(self):
        b=[0,0,0,0,0,0,0,0,0,0]
        j=[0,0,0,0,0,0,0,0,0,0]
        for i in range(len(self.Balkezesek)):
            b[self.balOldal[i]]=self.Balkezesek[i]
        for i in range(len(self.Jobbkezesek)):
            j[self.jobbOldal[i]]=self.Jobbkezesek[i]
        TODO

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
            bmom=hosszantiNy(balosPoz[i],balos)
            jmom=hosszantiNy(jobbPoz[j], jobbos)
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

def hosszantiNy( permut, evezosok):
        nyomatek=0.0
        tav=[0.675/2+4*0.675, 0.675/2+3*0.675, 0.675/2+2*0.675, 0.675/2+0.675, 0.675/2, -0.675/2, -0.675/2-0.675, -0.675/2-2*0.675, -0.675/2-3*0.675, -0.675/2-4*0.675]
        for i in range(len(permut)):
            s=evezosok[i].suly
            t=tav[permut[i]] 
            nyomatek+=s*t
        return nyomatek  
    
#főprogram 
if __name__ == "__main__":
    balos=[]
    jobbos=[]
    mindegy=[]
    hajok=[]
    fileName="evezosok.txt"
    beolvas(fileName)
    hajok=hosszanti_legjobbak(balos, jobbos)
    hajok.reverse()
    for i in range(3):
        hajok[i].kiiras()
    
    print("End")
