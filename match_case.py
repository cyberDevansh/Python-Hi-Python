command = "start" 
match command:
    case "start":
        print("Starting...")

    case "stop":
        print("Stopping...")

    case _:
        print("Unknown command")
#match case is like switch case in C    