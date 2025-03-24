import random
import string

class Lemmikki:
    def __init__(self, nimi: str, laji: str, syntymavuosi: int):
        self.nimi = nimi
        self.laji = laji
        self.syntymavuosi = syntymavuosi

def uusi_lemmikki(nimi: str, laji: str, syntymavuosi: int) -> Lemmikki:
    return Lemmikki(nimi, laji, syntymavuosi)

musti = uusi_lemmikki("Musti", "koira", 2017)
print(musti.nimi)
print(musti.laji)
print(musti.syntymavuosi)