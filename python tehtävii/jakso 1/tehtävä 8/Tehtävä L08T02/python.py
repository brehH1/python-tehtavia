def create_card(suit: str, value: int) -> tuple[str, int]:
    return (suit, value)

def create_deck() -> list[tuple[str, int]]:
    suits = ["hertta", "ruutu", "risti", "pata"]
    values = list(range(2, 15))  # Korttien arvot 2-14
    deck = []
    for suit in suits:
        for value in values:
            deck.append(create_card(suit, value))
    return deck

def format_card(card: tuple[str, int]) -> str:
    suit, value = card
    return f"{suit.capitalize()} {value}"

def print_deck(deck: list[tuple[str, int]]) -> None:
    for card in deck:
        print(format_card(card))

def main():
    deck = create_deck()
    print_deck(deck)

if __name__ == "__main__":
    main()