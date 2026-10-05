def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y


def main():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Choose an operation (1-4): ")

    if choice not in {"1", "2", "3", "4"}:
        print("Invalid choice. Please select 1, 2, 3, or 4.")
        return

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    operations = {
        "1": add,
        "2": subtract,
        "3": multiply,
        "4": divide,
    }

    try:
        result = operations[choice](num1, num2)
        print(f"Result: {result}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
