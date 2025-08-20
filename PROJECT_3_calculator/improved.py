import math

def calculator():
    print("=== Upgraded Calculator ===")
    print("Operations: +, -, *, /, ^ (power), sqrt (square root)")
    print("Type 'exit' anytime to quit.")
    
    memory = None  # for storing last result

    while True:
        user_input = input("\nEnter expression (or type 'exit'): ")

        if user_input.lower() == "exit":
            print("Calculator closed. 👋")
            break

        # special case: sqrt
        if user_input.startswith("sqrt"):
            try:
                num = float(user_input.split()[1])
                result = math.sqrt(num)
            except:
                result = "Error! Usage: sqrt number"
        
        else:
            try:
                # replace "ans" with memory value if used
                if memory is not None:
                    user_input = user_input.replace("ans", str(memory))
                
                # split input
                parts = user_input.split()
                if len(parts) != 3:
                    raise ValueError("Format: number operator number")
                
                num1, op, num2 = parts
                num1, num2 = float(num1), float(num2)

                if op == "+":
                    result = num1 + num2
                elif op == "-":
                    result = num1 - num2
                elif op == "*":
                    result = num1 * num2
                elif op == "/":
                    result = num1 / num2 if num2 != 0 else "Error: Division by zero!"
                elif op == "^":
                    result = num1 ** num2
                else:
                    result = "Invalid operator!"
            
            except Exception as e:
                result = f"Error: {e}"

        print("Result:", result)

        # store in memory if result is a number
        if isinstance(result, (int, float)):
            memory = result
            print("Saved in memory as 'ans'.")

# Run calculator
calculator()
