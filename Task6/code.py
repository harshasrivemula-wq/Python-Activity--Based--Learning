n = int(input("Enter number of batches: "))
threshold = float(input("Enter defect percentage threshold: "))

batches = []

for i in range(n):
    print("\nBatch", i + 1)
    product = input("Enter product name: ")
    quantity = int(input("Enter production quantity: "))
    defective = int(input("Enter defective units: "))

    batches.append((product, quantity, defective))

print("\n--- Quality Control Report ---")

for batch in batches:
    product = batch[0]
    quantity = batch[1]
    defective = batch[2]

    percentage = (defective / quantity) * 100

    print("\nProduct:", product)
    print("Production:", quantity)
    print("Defective:", defective)
    print("Defect Percentage:", round(percentage, 2), "%")

    if percentage > threshold:
        print("Status: Exceeds Quality Threshold")
    else:
        print("Status: Within Quality Limit")

print("\nQuality analysis completed.")
