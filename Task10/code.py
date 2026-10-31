students = []
events = []
resources = [("Lab", 20), ("Library", 50)]

while True:
    print("\n1.Add Student  2.Event  3.Resource  4.Report  5.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        attendance = float(input("Enter attendance: "))
        marks = float(input("Enter marks: "))
        students.append([name, attendance, marks])
        print("Student record added.")

    elif choice == 2:
        name = input("Enter event name: ")
        student = input("Enter student name: ")
        events.append((name, student))
        print("Event registration successful.")

    elif choice == 3:
        resource = input("Enter resource name: ")
        amount = int(input("Enter required quantity: "))
        resources.append((resource, amount))
        print("Resource allocated.")

    elif choice == 4:
        print("\n--- Student Records ---")
        for student in students:
            name, attendance, marks = student
            print(name, attendance, marks)

        print("\n--- Event Registrations ---")
        for event in events:
            event_name, student_name = event
            print(event_name, student_name)

        print("\n--- Resources ---")
        for resource, amount in resources:
            print(resource, amount)

    elif choice == 5:
        print("Campus management completed.")
        break

    else:
        print("Invalid choice.")
