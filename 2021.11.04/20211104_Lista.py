from random import *

def listaAlapok():
    #lista létrehozása
    alapok=[]
    for i in range(10):
        alapok.append(randint(1,50))
    alapok.append('alma')
    alapok.append('körte')
    print(alapok)
    # lista kiírása nszépen
    
    print(alapok[4]) # 4-es indexű elem (sorban az ötödik)
    print(len(alapok)) # lista elemszáma
    alapok.insert(4,'körte') # elem beszúrása adott helyre
    print(alapok.index('körte')) #elem indexe
    #print(alapok.index(55)) # hibaüzenettel áll meg, ha nincs benne a
    alapok.remove('körte') # adott elem törlése
    alapok.pop() # utolsó elem törlése
    del alapok[-1] # utolsó törlése
    del alapok[1] # 1. törlése 
    #alapok.clear # lista elemeit törli, lista megmarad
    #del alapok  # listát törli
    alapok.reverse() # sorrendet megfordítja
    alapok.sort()  # növekvő sorrendbe rakja
    alapok.reverse()
    print(alapok[5:]) # 5-ös indextől a végéig
    print(alapok[:4]) # elejétől az adott indexűig     (ezt már nem)
    print(alapok[-1]) # utolsó
    print(alapok[-2]) # utolsó előtti
    print(alapok[-2:]) # utolsó kettő
    print(alapok[3:5])
    alapok[6]='narancs'
    print(alapok[6]) 
    print()
    for item in alapok:
        print(item, end=" ")
    print()


def feladat1():
    elemszam=int(input("Add meg az elemek számát!"))
    szamok=[]
    for i in range(elemszam):
        szamok.append(randint(1,50))
    print(szamok) # ellenörzés miatt
    paratlandb=0
    for item in szamok:
        if item%2==1:
            paratlandb+=1
    print('A páratlanok száma',paratlandb)


def feladat2():
    elemszam=int(input("Add meg az elemek számát!"))
    szamok=[]
    for i in range(elemszam):
        szamok.append(randint(1,50))
    print(szamok) # ellenörzés miatt
    osszeg=0
    for item in szamok:
        if item%2==0:
            osszeg+=item
    print('A párosok összege',osszeg)
    
def feladat3():
    elemszam=int(input("Add meg az elemek számát!"))
    szamok=[]
    for i in range(elemszam):
        szamok.append(randint(1,50))
    print(szamok) # ellenörzés miatt
    for i in range(len(szamok)):
        if szamok[i]%2==0:
            print(i, '\t',szamok[i])




#listaAlapok()
#feladat1()
#feladat2()
feladat3()