pisteet = float(input("Kuinka paljon pisteitä? "))

if pisteet < 100:
    bonus = pisteet * 0.10
    print("Sait 10 % bonusta")
else:
    bonus = pisteet * 0.15
    print("Sait 15 % bonusta")

pisteet += bonus
print(f"Pisteitä on nyt {pisteet}")