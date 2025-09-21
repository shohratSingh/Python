# Employee Management System (EMS)
# A simplified system to manage employee data using dictionaries and functions

employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'Priya', 'age': 32, 'department': 'IT', 'salary': 65000},
    103: {'name': 'Rajesh', 'age': 29, 'department': 'Finance', 'salary': 55000}
}


def display_menu():
    print("----------EMPLOYEE MANAGEMENT SYSTEM----------")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Search for Employee")
    print("4. Exit")


def add_employee():
    print("\n--- ADD NEW EMPLOYEE ---")

    # Get and validate Employee ID
    for attempt in range(5):  # Allow up to 5 attempts
        try:
            emp_id = int(input("Enter Employee ID: "))
            if emp_id in employees:
                print(
                    f"Employee ID {emp_id} already exists! Please enter a unique ID.")
                continue
            break
        except ValueError:
            print("Please enter a valid numeric Employee ID.")
    else:
        print("Too many invalid attempts. Returning to main menu.")
        return

    # Get employee name
    for attempt in range(3):  # Allow up to 3 attempts
        name = input("Enter Employee Name: ").strip()
        if name:
            break
        print("Name cannot be empty!")
    else:
        print("Too many invalid attempts. Returning to main menu.")
        return

    # Get and validate age
    for attempt in range(3):  # Allow up to 3 attempts
        try:
            age = int(input("Enter Employee Age: "))
            if 18 <= age <= 100:
                break
            print("Please enter a valid age between 18 and 100.")
        except ValueError:
            print("Please enter a valid numeric age.")
    else:
        print("Too many invalid attempts. Returning to main menu.")
        return

    # Get department
    for attempt in range(3):  # Allow up to 3 attempts
        department = input("Enter Employee Department: ").strip()
        if department:
            break
        print("Department cannot be empty!")
    else:
        print("Too many invalid attempts. Returning to main menu.")
        return

    # Get and validate salary
    for attempt in range(3):  # Allow up to 3 attempts
        try:
            salary = float(input("Enter Employee Salary: "))
            if salary >= 0:
                break
            print("Salary cannot be negative.")
        except ValueError:
            print("Please enter a valid numeric salary.")
    else:
        print("Too many invalid attempts. Returning to main menu.")
        return

    # Store employee data
    employees[emp_id] = {
        'name': name,
        'age': age,
        'department': department,
        'salary': salary
    }

    print(f"\n Employee {name} (ID: {emp_id}) has been successfully added!")


def view_employees():
    print("\n--- ALL EMPLOYEES ---")

    if not employees:
        print("No employees available.")
        return

    # Display table header
    print(f"{'ID':<6} {'Name':<15} {'Age':<5} {'Department':<12} {'Salary':<10}")
    print("-" * 55)

    # Display each employee
    for emp_id, details in employees.items():
        print(f"{emp_id:<6} {details['name']:<15} {details['age']:<5} "
              f"{details['department']:<12} ₹{details['salary']:<9,.0f}")

    print(f"\nTotal Employees: {len(employees)}")


def search_employee():
    print("\n--- SEARCH EMPLOYEE ---")
    try:
        emp_id = int(input("Enter Employee ID to search: "))
    except ValueError:
        print("Please enter a valid numeric Employee ID.")
        return

    if emp_id in employees:
        print(f"\n Employee Found!")
        print("-" * 30)
        details = employees[emp_id]
        print(f"Employee ID: {emp_id}")
        print(f"Name: {details['name']}")
        print(f"Age: {details['age']}")
        print(f"Department: {details['department']}")
        print(f"Salary: ₹{details['salary']:,.0f}")
    else:
        print(f"\n Employee with ID {emp_id} not found.")


def main_menu():
    """Main function to run the Employee Management System"""
    print("Welcome to the Employee Management System!")

    for session in range(1000):  # Allow up to 1000 menu selections (effectively infinite)
        display_menu()

        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Please enter a valid number between 1 and 4.")
            input("\nPress Enter to continue...")
            continue

        if choice == 1:
            add_employee()
        elif choice == 2:
            view_employees()
        elif choice == 3:
            search_employee()
        elif choice == 4:
            print("Thank you for using Employee Management System!")
            break
        else:
            print("Invalid choice! Please select a number between 1 and 4.")

        # Pause before showing menu again
        input("\nPress Enter to continue...")


# Run the Employee Management System
if __name__ == "__main__":
    main_menu()
