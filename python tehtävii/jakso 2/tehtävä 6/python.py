import random
import string

def luo_salasana(pituus: int) -> str:
    return "".join(random.choices(string.ascii_lowercase, k=pituus))

def luo_hyva_salasana(pituus: int, sisaltaa_numeron: bool, sisaltaa_erikoismerkin: bool) -> str:
    merkit = string.ascii_lowercase
    if sisaltaa_numeron:
        merkit += string.digits
    if sisaltaa_erikoismerkin:
        merkit += "!?=+-()#"
    
    while True:
        salasana = "".join(random.choices(merkit, k=pituus))
        if any(c in string.ascii_lowercase for c in salasana) and \
           (not sisaltaa_numeron or any(c in string.digits for c in salasana)) and \
           (not sisaltaa_erikoismerkin or any(c in "!?=+-()#" for c in salasana)):
            return salasana

for i in range(10):
    print(luo_salasana(8))

print("\nParanneltu versio:")
for i in range(10):
    print(luo_hyva_salasana(8, True, True))
