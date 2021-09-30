# kerekítés round(mit, tizedesek száma)
print(round(3.1415, 3))
print(round(3.1415, 2))
#hatványozás0
print(pow(2,8))     #pow(alap, kitevő)
#abszolútérték abs(mit)
print(abs(-12))
print(abs(12))
print(min(12,7,9,45,3))
print(max(12,7,9,45,3))
# Pi

'''
import math
a=math.pi
print(a)
'''

from math import *   # A program elején helyezzük el.
a=pi
print(a)

#négyzetgyök -sqrt
print(sqrt(16))  #math.sqrt        (miből vonok gyököt)
# A felfelé kerekítés - ceil       (mit kerekítek)
print(ceil(3.56))
# A lefele kerekítés #math.floor   (mit)
print(floor(3.56))

# 1. A négyzet kerülete, területe.

a = float(input("Adja meg az oldalak hosszát! a="))
k=4*a
t=pow(a,2)
print("a(z)",a,"egység oldalú négyzet kerülete", k,"területe",t)
print("A négyzet kerülete",k)
print("A négyzet területe",t)


# 2. A téglalap kerülete, területe.


# 3. A kör kerülete  (2*r*PI), területe  (r^2*PI).


# 4. A kocka térfogata  (V=a^3), felszíne (A=6*a^2)


# 5. A derékszögű háromszög 2 befogóját kérd be, add meg az átfogót!
#        c=négyzetgyök(a^2+b^2)

