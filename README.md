# Testovac

testovac.py

- zo vstupneho suboru nahodne generuje otazky s odpovedami
- vstupny subor musi mat definovane otazky a odpovede
pomocou znaku na zaciatku riadku
- pomocou konfiguracnych premennych je mozne nastavit
niektore atributy zobrazovania, citania zo suboru
- program precita len riadky ktore obsahuju znaky (* @ x)
vsetko ostatne ignoruje (povazuje to za komentar)
- co jednotlive znaky na zaciatku riadku znamenaju:
	- (*) oznacuje zadanie (moze byt aj vo viacerych riadkoch)
	- (@) oznacuje NESPRAVNU odpoved
	- (x) oznacuje SPRAVNU odpoved
	
#### Konfiguracne premenne

| nazov premennej       | popis                                                 |
|-----------------------|-------------------------------------------------------|
| UCENIE                | Vypise spravnu odpoved                                |
| RANDOM                | Generuje odpovede nahodne                             |
| UKLADANIE_NESPRAVNYCH | V pripade nespravnej odpovede otazku znovu vygeneruje |
| POCET_ODPOVEDI        | nastavi kolko moznych odpovedi moze otazka obsahovat  |
| NESPRAVNE_ODPOVEDE    |                                                       |
	
