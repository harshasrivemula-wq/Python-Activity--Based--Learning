# Multi-Stage Scholarship Shortlisting

n = int(input("Enter number of candidates: "))
quota = int(input("Enter scholarship quota: "))
candidates = []

for i in range(n):
    print("\nCandidate", i + 1)
    name = input("Enter name: ")
    marks = float(input("Enter academic marks: "))
    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter family income: "))

    if marks >= 60 and attendance >= 75 and income <= 300000:
        candidates.append([name, marks])

for i in range(len(candidates)):
    for j in range(i + 1, len(candidates)):
        if candidates[i][1] < candidates[j][1]:
            candidates[i], candidates[j] = candidates[j], candidates[i]

print("\n--- Scholarship Shortlist ---")
count = 0

for candidate in candidates:
    if count < quota:
        print("Rank", count + 1, candidate[0], candidate[1])
        count += 1

if count == 0:
    print("No candidates selected.")
else:
    print("Total Selected:", count)

print("Scholarship selection completed.")
