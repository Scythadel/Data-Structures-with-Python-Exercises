def calc():
    num1 = None
    num2 = None
    arithmetic_operator = None
    arithmetic_operators = ["+", "-", "/", "*"]
    command = "Start" or "start"
    command = input("Please type start to begin calculations: ")
    while command != "" or command != "Stop":
        command = str(input("What would you like to perform?: "))
        if command == "Clear" or command == "clear":
            num1 = None
            num2 = None
            arithmetic_operator = None
        elif num1 == None:
            try:
                num1 = int(command)
            except ValueError:
                return "Enter a number"
        elif arithmetic_operator == None:
            for i in arithmetic_operators:
                if i == command:
                    arithmetic_operator = command
        else:
            try:
                num2 = int(command)
            except ValueError:
                return "Enter a number"
            


    if arithmetic_operator == "+":
        print(num1 + num2)
    elif arithmetic_operator == "-":
        print(num1 - num2)
    elif arithmetic_operator == "*":
        print(num1 / num2)
    elif arithmetic_operator == "/":
        print(num1 * num2)
    else:
        print('Enter a proper operator')

print(calc())
        
        

        



            
