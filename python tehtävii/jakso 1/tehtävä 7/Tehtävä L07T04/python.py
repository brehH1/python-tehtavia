class Pelikortti:
    def __init__(self, maa, arvo):
        self.maa = maa
        self.arvo = arvo

kortti1 = Pelikortti("pata", 7)
kortti2 = Pelikortti("hertta", 10)
kortti3 = Pelikortti("ruutu", 2)
kortti4 = Pelikortti("risti", 14)
kortti5 = Pelikortti("pata", 11)

print(kortti1.maa, kortti1.arvo)
print(kortti2.maa, kortti2.arvo)
print(kortti3.maa, kortti3.arvo)
print(kortti4.maa, kortti4.arvo)
print(kortti5.maa, kortti5.arvo)