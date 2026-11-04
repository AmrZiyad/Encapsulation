class MyClass:
    def __init__(self):
        # Correctly defining a private instance variable
        self.__privateVar = 27

    # Private method
    def __privMeth(self):
        print("I'm inside class MyClass")
        
    # Public function to access the private data/method
    def hello(self):
        # Accessing the mangled private variable using self
        print("Private Variable value:", self.__privateVar)

# Object creation and method call
foo = MyClass()
foo.hello()
