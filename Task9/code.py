n = int(input("Enter number of buildings: "))
energy_rate = float(input("Enter energy cost per unit: "))
water_rate = float(input("Enter water cost per unit: "))
buildings = []

for i in range(n):
    print("\nBuilding", i + 1)
    name = input("Enter building name: ")
    energy = float(input("Enter energy consumption: "))
    water = float(input("Enter water consumption: "))
    old_energy = float(input("Enter previous energy: "))

    energy_cost = energy * energy_rate
    water_cost = water * water_rate
    change = ((energy - old_energy) / old_energy) * 100
    score = energy + water
    buildings.append([name, energy, water, energy_cost, water_cost, change, score])

print("\n--- Campus Audit Report ---")
for b in buildings:
    print("\nBuilding:", b[0])
    print("Energy Cost:", b[3])
    print("Water Cost:", b[4])
    print("Energy Change:", round(b[5], 2), "%")

    if b[1] > 500 or b[2] > 1000:
        print("Status: Excessive Consumption")
    else:
        print("Status: Normal Consumption")

buildings.sort(key=lambda x: x[6], reverse=True)
print("\n--- Building Ranking ---")
for i in range(n):
    print(i + 1, buildings[i][0], "Score:", buildings[i][6])
