def calc():
    num1 = None
    num2 = None
    arithmetic_operator = None
    arithmetic_operators = ["+", "-", "/", "*"]
    command = "Start" or "start"
    while command != "" or command != "Stop":
        command = str(input("Enter the next value/operator: "))
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
            if command in arithmetic_operators:
                arithmetic_operator = command
        else:
            try:
                num2 = int(command)
                break
            except ValueError:
                return "Enter a number"
            
            
    if arithmetic_operator == "+":
        print(num1 + num2)
    elif arithmetic_operator == "-":
        print(num1 - num2)
    elif arithmetic_operator == "/":
        print(num1 / num2)
    elif arithmetic_operator == "*":
        print(num1 * num2)
    else:
        print('Enter a proper operator')

print(calc())