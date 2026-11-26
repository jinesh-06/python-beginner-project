import time

print("=" * 10, "Calculator", "=" * 10)

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 / num2
def power(num1, num2):
    return num1 ** num2
def modulus(num1, num2):
    if num2 == 0:
        return "Cannot perform modulus by zero"
    return num1 % num2
def view_history():
    try:
        with open("calculation_history.txt",'r') as file:
            history =file.readlines()
        if not history:
            print("No history found.")
        else:
            print("\nCalculation History:")
            for entry in history:
                print(entry.strip())
    except FileNotFoundError:
        print("No history found.")

def clear_history():
    confirm = input("Are you sure you want to clear the history? (y/n): ")

    if confirm.lower() == 'y':
        try:
            with open("calculation_history.txt", "w") as file:
                pass
            print("History cleared.")

        except OSError as e:
            print(f"Error clearing history: {e}")

    else:
        print("Clearing history cancelled.")

while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. power")
    print("6.modulus")
    print("7.view history")
    print("8.Exit")
    print("9.clear history")
    op = input("Enter choice (1/2/3/4/5/6/7/8/9): ")
    if op =='9':
        clear_history()
        continue
    elif op == '8':
        print("Exiting", end="")
        for i in range(3):
            print(".", end="")
            time.sleep(0.5)
        print("\nExited")
        break
    elif op =='7':
            view_history()
            continue
    elif op in ['1', '2', '3', '4','5','6']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input please enter numeric values.")
            continue

        if op == '1':
            result = add(num1, num2)
            symbol = "+"

        elif op == '2':
            result = subtract(num1, num2)
            symbol = "-"

        elif op == '3':
            result = multiply(num1, num2)
            symbol = "*"

        elif op == '4':
            result = divide(num1, num2)
            symbol = "/"

        elif op =='5':
            result =power(num1,num2)
            symbol ="**"

        elif op =='6':
            result =modulus(num1,num2)
            symbol ='%'

        if isinstance(result, (int, float)):
            calculation =f"{num1} {symbol} {num2} = {result}"
            print(calculation)

            with open("calculation_history.txt","a") as file:
                file.write(calculation + "\n")

        else:
            print(result)

    else:
        print("Invalid input!")