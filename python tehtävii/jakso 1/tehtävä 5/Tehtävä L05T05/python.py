def get_cost(kilometers, consumption, price_per_liter):
    fuel_needed = (kilometers / 100) * consumption
    cost = fuel_needed * price_per_liter
    return f"{round(cost, 2):.2f} €"

print(get_cost(100, 7.5, 1.88))
print(get_cost(220, 6.9, 1.88))