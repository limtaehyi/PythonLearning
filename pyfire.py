import fire

# Example 1
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


# Example 2
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

    def modulo(self, a, b):
        return a % b


# Example 3
class MathOperations:
    @staticmethod
    def power(base, exponent):
        return base ** exponent

    @staticmethod
    def square_root(value):
        return value ** 0.5


class App:
    def __init__(self):
        self.calculator = Calculator()
        self.math = MathOperations()

    def greet(self, name, greeting="Hello"):
        return greet(name, greeting)


if __name__ == "__main__":
    fire.Fire(App)

'''
 examples : 
 - python your_script.py greet John
 - python your_script.py calculator add 1 2
 - python your_script.py calculator subtract 1 2
 - python your_script.py calculator multiply 1 2
 - python your_script.py calculator divide 1 2
 - python your_script.py calculator modulo 1 2
 - python your_script.py math power 2 3
 - python your_script.py math square_root 4
'''