"""Write a Python program to create a class with the name "MyClass". In MyClass create a function
"sayHello()" which receives the name of the user as a parameter and prints "Hello, name!"."""
class MyClass:
    def sayHello(self, name):
        print(f"Hello, {name}!")
if __name__ == "__main__":
    obj = MyClass()
    name = input("Enter your name: ")
    obj.sayHello(name)