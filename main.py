class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def sub(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multi(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result


calc = Calculator()
# print(calc.add(20, 10))
# print(calc.sub(20, 10))
# print(calc.multi(5, 5))
# print(calc.divide(50, 5))

# print(calc.history)

print("\nThis Is Basic Calculator ")
print("Which Opration Do you want to Perform ? Choose From Below Option :")
print(
    """
Press 1 For Addition
Press 2 For Subtraction
Press 3 For Multiplication
Press 4 For Division
      """
)

Choice = int(input("What is You Choise : "))
num1 = int(input("Enter Frist Number : "))
num2 = int(input("Enter Second Number : "))

if Choice == 1:
    result = calc.add(num1, num2)
    print(f"{num1} + {num2} = {result}")

elif Choice == 2:
    result = calc.sub(num1, num2)
    print(f"{num1} - {num2} = {result}")

elif Choice == 3:
    result = calc.multi(num1, num2)
    print(f"{num1} * {num2} = {result}")

elif Choice == 4:
    result = calc.divide(num1, num2)
    print(f"{num1} / {num2} = {result}")
else:
    print("Invalid Choice")
