def get_number(prompt: str) -> float:
    while True:
        value = input(prompt).strip()
        try:
            return float(value)
        except ValueError:
            print("Invalid number. Please enter a numeric value.")


def calculate_result(num1: float, num2: float, operator: str) -> float | None:
    if operator == "+":
        return num1 + num2
    if operator == "-":
        return num1 - num2
    if operator == "*":
        return num1 * num2
    if operator == "/":
        if num2 == 0:
            print("Cannot divide by zero.")
            return None
        return num1 / num2

    print("Invalid operation. Please choose +, -, *, or /.")
    return None


def run_calculator() -> None:
    print("=== Simple Calculator ===")

    while True:
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        print("Operations: +  -  *  /")
        operator = input("Choose operation: ").strip()

        result = calculate_result(num1, num2, operator)
        if result is not None:
            print(f"Result: {result}")

        again = input("Do you want to perform another calculation? (y/n): ").strip().lower()
        if again != "y":
            print("Exiting Calculator. Goodbye!")
            break


if __name__ == "__main__":
    run_calculator()
