def MyOwnFunction():
    print("Improve Yourself Everyday and Don't Competete with others just competete yourself and become best version of yourserlf.")


if __name__ == "__main__":
    print("We are directly running this code from main file (not by importing)")
    MyOwnFunction()
    print(__name__)  
else:
    print("This code is run by importing from _module02.py file")
    MyOwnFunction()