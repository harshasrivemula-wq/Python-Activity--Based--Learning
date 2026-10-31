email = input("Enter student email: ")
reg = input("Enter registration ID: ")

print("\n--- Email Validation ---")

parts = email.split("@")

if len(parts) != 2:
    print("Malformed separator in email.")
else:
    username = parts[0]
    domain = parts[1]

    if username == "" or domain == "":
        print("Missing email component.")
    elif " " in email:
        print("Invalid character group: space found.")
    elif "." not in domain:
        print("Missing domain component.")
    elif username[0].isdigit():
        print("Invalid character group in username.")
    else:
        print("Email is valid.")

print("\n--- Registration ID Validation ---")

if reg == "":
    print("Missing registration ID.")
elif " " in reg:
    print("Malformed separator: space found.")
elif len(reg) < 6:
    print("Registration ID is too short.")
elif not reg[:3].isalpha():
    print("Invalid character group at beginning.")
elif not reg[3:].isdigit():
    print("Invalid character group: digits expected.")
else:
    print("Registration ID is valid.")
