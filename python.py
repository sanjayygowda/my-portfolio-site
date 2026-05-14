
def add(x, y):
   
    return x + y


def subtract(x, y):
   
    return x - y


def multiply(x, y):
    
    return x * y


def divide(x, y):
   
    if y == 0:
        return 
    return x / y


def calculator():
    """Main calculator function"""
    print("=" * 40)
    print("         Simple Calculator")
    print("=" * 40)
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    while True:
        choice = input("\nEnter choice (1/2/3/4/5): ")
        
        if choice == '5':
            print("\nThank you for using the calculator. Goodbye!")
            break
        
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == '1':
                    print(f"\n{num1} + {num2} = {add(num1, num2)}")
                
                elif choice == '2':
                    print(f"\n{num1} - {num2} = {subtract(num1, num2)}")
                
                elif choice == '3':
                    print(f"\n{num1} × {num2} = {multiply(num1, num2)}")
                
                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"\n{num1} ÷ {num2} = {result}")
            
            except ValueError:
                print("\nInvalid input! Please enter numeric values.")
        
        else:
            print("\nInvalid choice! Please select a valid operation.")


if __name__ == "__main__":
    calculator()
