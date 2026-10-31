n = int(input("Enter number of roads: "))
capacity = int(input("Enter road capacity: "))
traffic = []

for i in range(n):
    print("\nRoad", i + 1)
    name = input("Enter road name: ")
    count = int(input("Enter vehicle count: "))
    traffic.append([name, count])

peak = traffic[0][1]
peak_road = traffic[0][0]

print("\n--- Traffic Analysis ---")

for road in traffic:
    name = road[0]
    count = road[1]

    if count > peak:
        peak = count
        peak_road = name

    if count > capacity:
        level = "High - Exceeds Capacity"
    elif count >= capacity * 0.7:
        level = "Medium Congestion"
    else:
        level = "Low Congestion"

    print(name, ":", count, "-", level)

print("\nPeak Traffic Road:", peak_road)
print("Peak Vehicle Count:", peak)

print("\nRoads Exceeding Capacity:")
for road in traffic:
    if road[1] > capacity:
        print(road[0])
