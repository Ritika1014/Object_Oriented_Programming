class MyClass:
    def __new__(cls):
        print("Creating instance...")
        return super().__new__(cls)
    
    def __init__(self):
        print("Initializing instance...")

obj = MyClass()
