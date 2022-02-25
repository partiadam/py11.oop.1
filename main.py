'''
1.1 Feladat
Készíts egy programot, amelyben van egy Negyzet nevű osztály. Attribútuma legyen az oldal hossza. Rendelkezzen továbbá a kerület és terület számításra is egy-egy metódussal!
'''
'''
class Negyzet:
    def __init__(self, oldalhossz):
        self.oldalhossz = oldalhossz
    def kerulet(self):
        return self.oldalhossz * 4
    def terulet(self):
        return self.oldalhossz ** 2


negyzet = Negyzet(5)

print(f'A négyzet területe: {negyzet.terulet()}, a négyzet kerülete: {negyzet.kerulet()}')
'''


'''
1.2 Feladat
Módosítsd az előző programot úgy, hogy a metódus ne a kerület- illetve a területértékkel térjen vissza, hanem maga gondoskodjon ezen értékek kiírásáról egy egész mondatos formában.
'''

'''
class Negyzet:
    def __init__(self, oldalhossz):
        self.oldalhossz = oldalhossz
    def kiiras(self):
        return (f'A négyzet területe:', self.oldalhossz **2, 'a négyzet kerülete:', self.oldalhossz * 4)


negyzet = Negyzet(3)
print(negyzet.kiiras())
'''

'''
1.3 Feladat
Az 1.1 feladatban meghatározottak szerint készíts egy programot, amely a felhasználótól egymás után bekér négyzetek oldalhosszát egészen addíg, amíg a felhasználó 0 értéket nem ad meg! Ezen adat alapján a program hozzon létre negyzet objektumokat, melyeket egy listában tárol! A program írja ki a megadott négyzetek oldalhosszát, kerületét és területét!
'''

'''
lista = []


class Negyzet:
    def __init__(self, oldalhossz):
        self.oldalhossz = oldalhossz
        
    def kerulet(self):
        return self.oldalhossz * 4
        
    def terulet(self):
        return self.oldalhossz ** 2


while True:
    beker = int(input('Szám: '))
    lista.append(beker)
    if beker == 0:
        break

for i in lista:
    negyzet1 = Negyzet(i)

    print(f'A négyzet területe: {negyzet1.terulet()}, a négyzet kerülete: {negyzet1.kerulet()} ')
'''

'''
2. Feladat
Készíts egy programot, amely objektumorientált módon tartja nyilván kutyák adatait (név, életkor, nem)! A nevét a felhasználó adja meg, az életkorát és a nemét véletlenszerűen határozza meg a program! Befejezésként a program a képernyőre írja ki a megadott kutyák adatait!
'''

'''
from random import choice, randint


nemek = ['fiu', 'lany']

class Kutya:
    def __init__(self, nev):
        self.nev = nev
        kor = randint(1,15)
        nem = choice(nemek)
        print(f'A kutya neve: {self.nev}, kora: {kor}, neme: {nem}')


kutya = Kutya('feri')
'''




