def add(x,y) :             
    print(f"The summation of {x} and {y} = {x+y}")
def multiply(x,y) : 
    print(f"The multiplication of {x} and {y} = {x*y}")
def sub(x,y) : 
    print(f"The subtraction of {x} and {y} = {x-y}")
def divide(x,y) : 
    if y == 0 :
        print("undefined! cannot divide by zero")
    else : 
        print(f"The division of {x} and {y} = {x/y}")

print("Python Calculator")

while True : 
    print("Please choose an operation to do : + , - , * , / or type 'exit' to exit the calculator")
    choice = input("Select an operation : ")
    if choice == 'exit' :
        print("closing the calculator..")
        break
    
    num1 = float(input("Please enter the first number : "))
    num2 = float(input("Please enter the second number : "))
    
    match choice : 
        case '+' :
            add(num1,num2)
        case '-' :
            sub(num1,num2)
        case '*' : 
            multiply(num1,num2)
        case '/' :
            divide(num1,num2)
        case _ :
            print("Invalid operation selected!")