def get_fuel(kilometers, consumption):
    fuel = (kilometers / 100) * consumption
    return f"{round(fuel, 1)} ltr"

print(get_fuel(100, 7.5))
print(get_fuel(220, 6.9))