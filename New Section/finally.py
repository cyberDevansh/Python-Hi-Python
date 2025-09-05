def firsttry():
        try:
            a = int (input("Enter a number:"))
            print(a)
            return

        except Exception as e:
              print(e)
              return

        finally:
              print("Hey this is inside finally.")
        


firsttry()


#finally runs in all cases even if return is used in the function 


def secondtry():
        try:
            a = int (input("Enter a number:"))
            print(a)
            return

        except Exception as e:
              print(e)
              return

    
        print("Hey this is inside finally.")  # now this will not run but if we are outside the function then we finally works same as print outside the loop so the main use of the finally is inside the function to run even after the return 
        


secondtry()
