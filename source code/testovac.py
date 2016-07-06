__author__ = 'alienson'

"""
============================================================
Testovac
============================================================
- zo vstupneho suboru nahodne generuje otazky s odpovedami
- vstupny subor musi mat definovane otazky a odpovede
pomocou znaku na zaciatku riadku
- pomocou konfiguracnych premennych je mozne nastavit
niektore atributy zobrazovania, citania zo suboru
- program precita len riadky ktore obsahuju znaky (* @ x)
vsetko ostatne ignoruje (povazuje to za komentar)
- co jednotlive znaky na zaciatku riadku znamenaju:
    (*) oznacuje zadanie (moze byt aj vo viacerych riadkoch)
    (@) oznacuje NESPRAVNU odpoved
    (x) oznacuje SPRAVNU odpoved
============================================================
"""

import random
import copy

"""
Konfiguracne premenne

UCENIE                  - Vypise spravnu odpoved
NESPRAVNE_ODPOVEDE      -
RANDOM                  - Generuje odpovede nahodne
UKLADANIE_NESPRAVNYCH   - V pripade nespravnej odpovede otazku znovu vygeneruje
POCET_ODPOVEDI          - nastavi kolko moznych odpovedi moze otazka obsahovat
"""
UCENIE                  = False
NESPRAVNE_ODPOVEDE      = True
RANDOM                  = True
UKLADANIE_NESPRAVNYCH   = True
POCET_ODPOVEDI          = 4
MAX_ZNAKOV_V_RIADKU     = 100

class Testovac(object):
    def __init__(self, subor):
        self.priklady = dict()
        self.zleOdpovedane = set()
        subor = open(subor, "r", encoding="utf8")
        zadanie = []
        moznosti = []
        for riadok in subor.read().split("\n"):
            if riadok.startswith("*"):
                zadanie.append(riadok[1:].strip())
            elif riadok.startswith("x"):
                moznosti.append((riadok[1:].strip(),True))
            elif riadok.startswith("@"):
                moznosti.append((riadok[1:].strip(),False))

            if len(moznosti) == POCET_ODPOVEDI:
                self.priklady[tuple(zadanie)] = moznosti
                zadanie = []
                moznosti = []
        self.povodnePriklady = copy.deepcopy(self.priklady)

    def zacni(self):
        while bool(self.priklady):
            kluc = random.choice(list(self.priklady.keys()))
            for riadok in kluc:
                print(riadok)
            cislo = 1
            if RANDOM:
                random.shuffle(self.priklady[kluc])
            if not NESPRAVNE_ODPOVEDE:
                self.vypisMoznosti(self.priklady[kluc])
            elif UCENIE:
                print("Spravna odpoved je cislo: ", self.vypisSpravnuOdpoved(self.priklady[kluc]))
                self.vypisMoznosti(self.priklady[kluc])
            else:
                self.vypisMoznosti(self.priklady[kluc])


            if self.kontroluj(kluc):
                self.priklady.pop(kluc)
        if len(self.zleOdpovedane) != 0:
            if UKLADANIE_NESPRAVNYCH:
                print("Zvládol si odpovedať na všetky úlohy správne,")
                print("ale niektoré si nevedel na prvý krát.")
                print("Bolo ich =",len(self.zleOdpovedane),"= a toto su oni:")
            else:
                print("Nezvládol si odpovedať na všetky úlohy správne,")
                print("Bolo ich =", len(self.zleOdpovedane), "= a toto su oni:")
            cislo = 0
            for zleOtazky in self.zleOdpovedane:
                cislo += 1
                print(cislo,end=".) ")
                print(zleOtazky[0])
                print("Správna odpoved:", end=" ")
                for spravnaMoznost in self.povodnePriklady[zleOtazky]:
                    if spravnaMoznost[1]:
                        print(spravnaMoznost[0])
                
        else:
            print("GRATULUJEM !!!")
            print("Zvládol si odpovedať na všetky úlohy správne")

    def vypisSpravnuOdpoved(self, moznosti):
        for i in range(len(moznosti)):
            if moznosti[i][1]:
                return i+1

    def vypisMoznosti(self, moznosti):
        cislo = 1
        for moznost in moznosti:
            # if UCENIE:
            if len(moznost[0]) <= MAX_ZNAKOV_V_RIADKU:
                if NESPRAVNE_ODPOVEDE:
                    print(str(cislo) + ".)", moznost[0])
                else:
                    if moznost[1]:
                        print(str(cislo) + ".)", moznost[0])
            else:
                if NESPRAVNE_ODPOVEDE:
                    print(str(cislo) + ".)", end=" ")
                    dlzka = 0
                    for slovo in moznost[0].split():
                        print(slovo, end=" ")
                        dlzka += len(slovo)+1
                        if dlzka >= 100:
                            print()
                            dlzka = 0
                else:
                    if moznost[1]:
                        print(str(cislo) + ".)", end=" ")
                        dlzka = 0
                        for slovo in moznost[0].split():
                            print(slovo, end=" ")
                            dlzka += len(slovo) + 1
                            if dlzka >= 100:
                                print()
                                dlzka = 0
                print()
            cislo += 1

    def kontroluj(self, kluc):
        while 1:
            moznost = input()
            try:
                moznost = int(moznost)-1
                if self.priklady[kluc][moznost][1]:
                    print("Spravne\n")
                    return True
                else:
                    print("Zle!! Správna odpoved je\n")
                    self.zleOdpovedane.add(kluc)
                    for spravnaMoznost in self.priklady[kluc]:
                        if spravnaMoznost[1]:
                            print(spravnaMoznost[0])
                    print()
                    if UKLADANIE_NESPRAVNYCH:
                        return False
                    return True
            except:
                print("zly vstup! Napis len cisla 1-"+str(len(self.priklady[kluc])))

if __name__ == "__main__":
    t = Testovac("example.txt")
    t.zacni()
