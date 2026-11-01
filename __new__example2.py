class A:
    def __new__(cls):
        print("Creating instance")
        return "Hello, World!"

print(A())