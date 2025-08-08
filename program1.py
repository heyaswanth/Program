class Calculator:
    def __init__(self, a, b): 
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Error: Division by zero"


def main():
    print("Simple Calculator Using Class")
    try:
        print("\nOperations:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        choice = input("Choose operation (1/2/3/4): ")

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    calc = Calculator(num1, num2)

    
   

    if choice == '1':
        print("Result:", calc.add())
    elif choice == '2':
        print("Result:", calc.subtract())
    elif choice == '3':
        print("Result:", calc.multiply())
    elif choice == '4':
        print("Result:", calc.divide())
    else:
        print("Invalid choice.")

if __name__== "__main__": 
    main()
