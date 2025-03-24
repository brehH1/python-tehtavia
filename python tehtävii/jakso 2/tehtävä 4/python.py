class Auto:
    def __init__(self):
        self.__bensaa = 0  
        self.__ajetut_km = 0
    
    def tankkaa(self):
        self.__bensaa = 60
    
    def aja(self, km: int):
        ajettava_matka = min(km, self.__bensaa)
        self.__ajetut_km += ajettava_matka
        self.__bensaa -= ajettava_matka
    
    def __str__(self):
        return f"Auto: ajettu {self.__ajetut_km} km, bensaa {self.__bensaa} litraa"

# Esimerkkikäyttö
auto = Auto()
print(auto)
auto.tankkaa()
print(auto)
auto.aja(20)
print(auto)
auto.aja(50)
print(auto)
auto.aja(10)
print(auto)
auto.tankkaa()
auto.tankkaa()
print(auto)
