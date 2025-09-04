class Demo:

    # 1. Instance method (needs 'self')
    def instance_method(self, x):
        print(f"[Instance] self = {self}, x = {x}")

    # 2. Class method (needs 'cls')
    @classmethod
    def class_method(cls, y):
        print(f"[Class] cls = {cls}, y = {y}")

    # 3. Static method (no self, no cls)
    @staticmethod
    def static_method(z):
        print(f"[Static] z = {z}")


# ------------------- Testing --------------------------------------

obj = Demo()   # create an object

# Instance method
obj.instance_method(10)        # call using object
Demo.instance_method(obj, 10)  # same call explicitly

# Class method
obj.class_method(20)           # can call from object
Demo.class_method(20)          # or directly from class

# Static method
obj.static_method(30)          # can call from object
Demo.static_method(30)         # or directly from class
