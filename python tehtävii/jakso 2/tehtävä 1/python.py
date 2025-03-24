def rivi_oikein(sudoku: list, rivi_nro: int) -> bool:
    rivin_numerot = sudoku[rivi_nro]
    numerot = set()
    
    for numero in rivin_numerot:
        if numero in numerot and numero != 0:
            return False
        numerot.add(numero)
    
    return True

sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

print(rivi_oikein(sudoku, 0))  # True
print(rivi_oikein(sudoku, 1))  # False
