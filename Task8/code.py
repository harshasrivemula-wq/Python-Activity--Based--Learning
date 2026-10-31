n = int(input("Enter number of routes: "))
routes = []

for i in range(n):
    print("\nRoute", i + 1)
    name = input("Enter route name: ")
    passengers = int(input("Enter passengers: "))
    capacity = int(input("Enter bus capacity: "))
    time = float(input("Enter journey time: "))
    fuel = float(input("Enter fuel used: "))

    efficiency = passengers / fuel
    routes.append([name, passengers, capacity, time, fuel, efficiency])

print("\n--- Bus Route Analysis ---")

best = routes[0]
for route in routes:
    name = route[0]
    passengers = route[1]
    capacity = route[2]
    time = route[3]
    fuel = route[4]
    efficiency = route[5]

    print("\nRoute:", name)
    print("Passengers:", passengers)
    print("Journey Time:", time)
    print("Fuel Used:", fuel)
    print("Efficiency:", round(efficiency, 2))

    if passengers > capacity:
        print("Status: Overloaded")
    else:
        print("Status: Normal")

    if efficiency > best[5]:
        best = route

print("\nMost Efficient Route:", best[0])
print("Efficiency:", round(best[5], 2))
