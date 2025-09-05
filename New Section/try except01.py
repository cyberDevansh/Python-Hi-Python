def error_demo():
    try:
        # 1. ZeroDivisionError
        x = 10 / 0

        # 2. ValueError
        num = int("abc")

        # 3. IndexError
        mylist = [1, 2, 3]
        print(mylist[5])

        # 4. KeyError
        mydict = {"a": 1}
        print(mydict["b"])

        # 5. TypeError
        result = "5" + 5

        # 6. AttributeError
        none_obj = None
        none_obj.upper()

        # 7. FileNotFoundError
        with open("no_file.txt", "r") as f:
            f.read()

        # 8. ImportError
        import non_existing_module

    except ZeroDivisionError as e:
        print(" Cannot divide by zero:", e)

    except ValueError as e:
        print(" Invalid value:", e)

    except IndexError as e:
        print(" List index out of range:", e)

    except KeyError as e:
        print(" Dictionary key not found:", e)

    except TypeError as e:
        print(" Wrong type used:", e)

    except AttributeError as e:
        print(" Attribute not found:", e)

    except FileNotFoundError as e:
        print(" File not found:", e)

    except ImportError as e:
        print(" Import error:", e)

    except Exception as e:
        print("⚠️ Some other error occurred:", e)

    finally:
        print("✅ Done checking errors.")


error_demo()






#ZeroDivisionError → dividing by 0

# ValueError → wrong type for conversion (e.g., "abc" → int)
# IndexError → list index out of range
# KeyError → dict key not found
# TypeError → invalid operation between types
# AttributeError → attribute doesn’t exist
# FileNotFoundError → file doesn’t exist
# ImportError → trying to import a missing module
# Exception → catch-all for anything else
# finally → always runs (cleanup, closing files, etc.)