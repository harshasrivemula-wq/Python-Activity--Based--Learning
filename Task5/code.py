n = int(input("Enter number of locations: "))
points = []

for i in range(n):
    print("\nLocation", i + 1)
    x = float(input("Enter x coordinate: "))
    y = float(input("Enter y coordinate: "))
    points.append((x, y))

longest = 0
longest_segment = 0

print("\n--- Route Distances ---")

for i in range(n - 1):
    x1, y1 = points[i]
    x2, y2 = points[i + 1]
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    print("Segment", i + 1, "Distance:", round(distance, 2))

    if distance > longest:
        longest = distance
        longest_segment = i + 1

print("\nLongest Route Segment:", longest_segment)
print("Longest Distance:", round(longest, 2))
print("Route analysis completed.")
