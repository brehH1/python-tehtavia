def tallenna_henkilo(henkilo: tuple):
    with open("henkilot.csv", "a", encoding="utf-8") as tiedosto:
        tiedosto.write(f"{henkilo[0]};{henkilo[1]};{henkilo[2]}\n")


tallenna_henkilo(("Kimmo Kimmonen", 37, 175.5))