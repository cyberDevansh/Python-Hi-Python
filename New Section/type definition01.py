age: int = 20
name: str = "Alice"
is_student: bool = True

def greet(name: str, age: int) -> str:     #-> str → means the function will return a string
    return f"My name is {name} and I am {age} years old."

print(greet("Bob", 25))
