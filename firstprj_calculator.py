# first functions ... 
import os

def save_history(operation, result):
    # Get the path ...
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "history.txt")

    with open(file_path, "a") as file:
        file.write(f"{operation} = {result}\n")
    
def clr_screen():
    os.system('cls')
        
# math functions ...
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y
def power(x, y):
    return x**y

def square_root(x):
    import math
    if x < 0 :
        return "Error: can't be done with a negative number!"
    return math.sqrt(x)

# Menu ...
while True:
    print("\nSimple Calculator")
    print("Select operation:")
    print("1)Add, 2)Subtract, 3)Multiply, 4)Divide, 5)power(x^y), 6)square root")
    # print("2. Subtract")
    # print("3. Multiply")
    # print("4. Divide")
    # print("5.power(x^y)")
    # print("6.square root")
    print("7. Exit")

    
    choice = input("Enter choice (1 to 7): ")

    if choice == '7':
        clr_screen()
        print("Goodbye! 👋")
        break

    if choice not in ['1', '2', '3', '4', '5', '6']:
        print("Invalid input. Please try again.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        if choice != '6' :
            num2 = float(input("Enter second number: "))
    
    except ValueError:
        print("Invalid number. Please enter numeric values.")
        continue

    if choice == '1':
        result = add(num1, num2)
        save_history(f"{num1} + {num2}",result)
        print(f"{num1}+{num2} =",result)
        input('To continue press Enter !')
        clr_screen()
    
    elif choice == '2':
        result = subtract(num1, num2)
        save_history(f"{num1} - {num2}",result)
        print(f"{num1}-{num2} =",result)
        input('To continue press Enter !')
        clr_screen()
    
    elif choice == '3':
        result = multiply(num1, num2)
        save_history(f"{num1} * {num2}",result)
        print(f"{num1}*{num2} =",result)
        input('To continue press Enter !')
        clr_screen()
    
    elif choice == '4':
        result = divide(num1, num2)
        save_history(f"{num1} / {num2}",result)
        print(f"{num1}/{num2} =",result)
        input('To continue press Enter !')
        clr_screen()
    
    elif choice == '5':
        result = power(num1, num2)
        save_history(f"{num1} ^ {num2}",result)
        print(f"{num1}^{num2} =",result)
        input('To continue press Enter !')
        clr_screen()
    
    elif choice == '6':
        result = square_root(num1)
        save_history(f"{num1}'s root ",result)
        print(f"{num1}'s root ",result) 
        input('To continue press Enter !')
        clr_screen()