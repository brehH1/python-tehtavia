class Kirja:
    def __init__(self, nimi: str, kirjoittaja: str, genre: str, vuosi: int):
        self.nimi = nimi
        self.kirjoittaja = kirjoittaja
        self.genre = genre
        self.vuosi = vuosi

def vanhempi_kirja(kirja1: Kirja, kirja2: Kirja):
    if kirja1.vuosi < kirja2.vuosi:
        print(f"{kirja1.nimi} on vanhempi, se kirjoitettiin {kirja1.vuosi}")
    elif kirja2.vuosi < kirja1.vuosi:
        print(f"{kirja2.nimi} on vanhempi, se kirjoitettiin {kirja2.vuosi}")
    else:
        print(f"{kirja1.nimi} ja {kirja2.nimi} kirjoitettiin {kirja1.vuosi}")


python = Kirja("Fluent Python", "Luciano Ramalho", "ohjelmointi", 2015)
everest = Kirja("Huipulta huipulle", "Carina Räihä", "elämänkerta", 2010)
norma = Kirja("Norma", "Sofi Oksanen", "rikos", 2015)

vanhempi_kirja(python, everest)
vanhempi_kirja(python, norma)