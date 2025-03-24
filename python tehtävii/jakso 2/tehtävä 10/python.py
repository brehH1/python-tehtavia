class Tavara:
    def __init__(self, nimi: str, paino: int):
        self.__nimi = nimi
        self.__paino = paino

    def nimi(self):
        return self.__nimi

    def paino(self):
        return self.__paino

    def __str__(self):
        return f"{self.__nimi} ({self.__paino} kg)"


class Matkalaukku:
    def __init__(self, maksimipaino: int):
        self.__maksimipaino = maksimipaino
        self.__tavarat = []

    def lisaa_tavara(self, tavara: Tavara):
        if self.paino() + tavara.paino() <= self.__maksimipaino:
            self.__tavarat.append(tavara)

    def __str__(self):
        tavaroiden_lkm = len(self.__tavarat)
        yhteispaino = self.paino()
        lkm_teksti = "tavara" if tavaroiden_lkm == 1 else "tavaraa"
        return f"{tavaroiden_lkm} {lkm_teksti} ({yhteispaino} kg)"

    def tulosta_tavarat(self):
        for tavara in self.__tavarat:
            print(tavara)

    def paino(self):
        return sum(tavara.paino() for tavara in self.__tavarat)

    def raskain_tavara(self):
        return max(self.__tavarat, key=lambda t: t.paino(), default=None)


class Lastiruuma:
    def __init__(self, maksimipaino: int):
        self.__maksimipaino = maksimipaino
        self.__matkalaukut = []

    def lisaa_matkalaukku(self, matkalaukku: Matkalaukku):
        if self.paino() + matkalaukku.paino() <= self.__maksimipaino:
            self.__matkalaukut.append(matkalaukku)

    def __str__(self):
        laukkujen_lkm = len(self.__matkalaukut)
        tilaa_jaljella = self.__maksimipaino - self.paino()
        laukku_teksti = "matkalaukku" if laukkujen_lkm == 1 else "matkalaukkua"
        return f"{laukkujen_lkm} {laukku_teksti}, tilaa {tilaa_jaljella} kg"

    def tulosta_tavarat(self):
        for laukku in self.__matkalaukut:
            laukku.tulosta_tavarat()

    def paino(self):
        return sum(laukku.paino() for laukku in self.__matkalaukut)

kirja = Tavara("Aapiskukko", 2)
puhelin = Tavara("Nokia 3210", 1)
tiiliskivi = Tavara("Tiiliskivi", 4)

matkalaukku = Matkalaukku(10)
matkalaukku.lisaa_tavara(kirja)
matkalaukku.lisaa_tavara(puhelin)
matkalaukku.lisaa_tavara(tiiliskivi)

print("Matkalaukussa on seuraavat tavarat:")
matkalaukku.tulosta_tavarat()

print(f"Yhteispaino: {matkalaukku.paino()} kg")

raskain = matkalaukku.raskain_tavara()
print(f"Raskain tavara: {raskain}")

lastiruuma = Lastiruuma(1000)
lastiruuma.lisaa_matkalaukku(matkalaukku)

print("Ruuman matkalaukuissa on seuraavat tavarat:")
lastiruuma.tulosta_tavarat()