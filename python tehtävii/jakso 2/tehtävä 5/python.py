def tulosta_henkilot(henkilotiedot: list):
    tulosteet = []
    for henkilo in henkilotiedot:
        nimi = henkilo["nimi"]
        ika = henkilo["ika"]
        harrastukset = ", ".join(henkilo["harrastukset"])
        tulosteet.append(f"{nimi} {ika} vuotta ({harrastukset})")

    print(" ".join(tulosteet))

henkilot = [
    {"nimi": "Pekka Pythonisti", "ika": 27, "harrastukset": ["koodaus", "kutominen"]},
    {"nimi": "Jaana Javanainen", "ika": 24, "harrastukset": ["koodaus", "kalliokiipeily", "lukeminen"]}
]
tulosta_henkilot(henkilot)
