def feladat24():
    szam=float(input("Kérek egy számot!"))
    while szam!=0:
        szam=float(input("Kérek egy másik számot!"))



def feladat25():
    szam=float(input("Kérek egy pozitív számot!"))
    while szam<=0:
        szam=float(input("Nem pozitív számot adtál, addj egy pozitívat!"))


def feladat26():
    szam=float(input("Kérek egy tíznél kissebb számot!"))
    osszeg = szam
    while szam>=10:
        szam=float(input("Nagyobb mint tíz kérek egy tíznél kissebb számot!"))
        osszeg += szam
    print("A számok összege",osszeg)

#itt kezdődik a program
#feladat24()
#feladat25()
feladat26()