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
def view_history(history):
    if not history:
        print("No calculations yet.")
    else:
        print("\nCalculation History:")
        for entry in history:
            print(entry)

history=[]
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
    op = input("Enter choice (1/2/3/4/5/6/7/8): ")

    if op == '8':
        print("Exiting", end="")
        for i in range(3):
            print(".", end="")
            time.sleep(1)
        print("\nExited")
        break
    elif op =='7':
            view_history(history)
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
            calculation =f"\n{num1} {symbol} {num2} = {result}"
            print(calculation)
            history.append(calculation)

            with open("calculation_history.txt","a") as file:
                file.write(calculation + "\n")

        else:
            print(result)

    else:
        print("Invalid input!")