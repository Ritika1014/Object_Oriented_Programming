class A:
    def __new__(cls):
        print("Creating instance")

    def __init__(self):
        print("Initializing instance")

print(A())