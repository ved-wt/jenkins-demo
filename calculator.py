# calculator.py

class Calculator:
    def add(self, a, b):
        print(f"Addition of {a} and {b} is: {a + b}")
        return a + b

    def sub(self, a, b):
        print(f"Subtraction of {a} and {b} is: {a - b}")
        return a - b

    def mul(self, a, b):
        print(f"Multiplication of {a} and {b} is: {a * b}")
        return a * b

    def div(self, a, b):
        if b == 0:
            print("Error: Division by zero is not allowed.")
            return None
        print(f"Division of {a} and {b} is: {a / b}")
        return a / b

if __name__ == "__main__":
    c1 = Calculator()
    c1.add(10, 20)
    c1.sub(30, 40)
    c1.mul(10, 10)
    c1.div(40, 5)