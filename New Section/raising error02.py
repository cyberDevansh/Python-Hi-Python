def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    print(f"Age set to {age}")

set_age(25)   # works
set_age(-3)   # raises ValueError
