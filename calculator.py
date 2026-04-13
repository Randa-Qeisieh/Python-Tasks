def add(x,y): return x+y
def multiply(x,y): return x*y
def sub(x,y): return x-y
def divide(x,y): return x/y

while True : 
    print("Python Calculator")
    print("Please choose an operation to do : + , - , * , / or type 'exit' to exit the calculator")
    choice = input("Select an operation : ")
    if choice == 'exit' :
        print("closing the calculator..")
        break
    
    if choice not in ['+', '-', '*', '/']:
        print("Invalid operation selected! Please try again.")
        continue
    
    num1 = float(input("Please enter the first number : "))
    num2 = float(input("Please enter the second number : "))
    
    match choice : 
        case '+' :
            print(f"The summation of {num1} and {num2} = {add(num1,num2)}")
        case '-' :
            print(f"The subtraction of {num1} and {num2} = {sub(num1,num2)}")
        case '*' : 
            print(f"The multiplication of {num1} and {num2} = {multiply(num1,num2)}")
        case '/' :
            print(f"The division of {num1} and {num2} = {divide(num1,num2)}")
        case _ :
            print("Invalid operation selected!")

