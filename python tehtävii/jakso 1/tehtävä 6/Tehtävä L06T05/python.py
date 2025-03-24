def calculate_discount(quantity):
    if 10 <= quantity <= 49:
        return 5
    elif 50 <= quantity <= 99:
        return 10
    elif quantity >= 100:
        return 15
    else:
        return 0

def calculate_final_price(price, quantity, discount_percentage):
    total_price = price * quantity
    discount_amount = total_price * (discount_percentage / 100)
    final_price = total_price - discount_amount
    return final_price

def main():
    price = float(input("Syötä tuotteen hinta: "))
    quantity = int(input("Syötä ostettava määrä: "))
    discount_percentage = calculate_discount(quantity)
    final_price = calculate_final_price(price, quantity, discount_percentage)
    print(f"Alennusprosentti: {discount_percentage}%")
    print(f"Lopullinen hinta: {final_price:.2f} euroa")

if __name__ == "__main__":
    main()