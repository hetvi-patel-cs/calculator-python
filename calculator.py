import math

while True:
    print("\n--- Python Calculator ---")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Square Root (√)")
    print("7. Percentage (%)")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == '8':
        print("Exiting calculator.. Goodbye!")
        break

    # Operations that require two numbers
    if choice in ['1','2','3','4','5','7']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

    # Operations that require one number
    if choice == '6':
        try:
            num = float(input("Enter the number: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

    # Perform the chosen operation
    if choice == '1':
        print("Result:", num1 + num2)
    elif choice == '2':
        print("Result:", num1 - num2)
    elif choice == '3':
        print("Result:", num1 * num2)
    elif choice == '4':
        if num2 == 0:
            print("Cannot divide by zero!")
        else:
            print("Result:", num1 / num2)
    elif choice == '5':
        print("Result:", num1 ** num2)
    elif choice == '6':
        if num < 0:
            print("Cannot take square root of a negative number!")
        else:
            print("Result:", math.sqrt(num))
    elif choice == '7':
        print("Result:", (num1 / num2) * 100, "%")
    else:
        print("Invalid choice! Please enter a number from 1 to 8.")
