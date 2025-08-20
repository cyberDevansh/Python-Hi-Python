def calculator():
    rounds = 3
    for i in range(rounds):
        print(f"\nRound {i+1}: Simple Calculator")
        
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        op = input("Choose operation (+, -, *, /): ")

        if op == "+":
            print("Result =", num1 + num2)
        elif op == "-":
            print("Result =", num1 - num2)
        elif op == "*":
            print("Result =", num1 * num2)
        elif op == "/":
            if num2 != 0:
                print("Result =", num1 / num2)
            else:
                print("Error: Division by zero not allowed!")
        else:
            print("Invalid operation!")

   
    choice = input("\nDo you want to continue? (y/n): ")
    if choice.lower() == "y":
        calculator()
    else:
        print("Goodbye 👋")

calculator()
