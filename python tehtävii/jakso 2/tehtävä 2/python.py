def pelaa_siirto(lauta: list, x: int, y: int, nappula: str) -> bool:
    if not (0 <= x <= 2 and 0 <= y <= 2):
        return False
    
    if lauta[y][x] == "":
        lauta[y][x] = nappula
        return True
    
    return False

lauta = [["", "", ""], ["", "", ""], ["", "", ""]]
print(pelaa_siirto(lauta, 2, 0, "X"))  # True
print(lauta)  # [['', '', 'X'], ['', '', ''], ['', '', '']]
