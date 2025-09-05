class MyCustomError(Exception):
    pass

def process_data(data):
    if data == "":
        raise MyCustomError("Empty data is not allowed!")
    print(f"Processing: {data}")

process_data("Hello")  
process_data("")       # raises MyCustomError
