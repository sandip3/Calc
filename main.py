import math


class Calculator:
    def __init__(self):
        self.history = []

    # basic Math
    def add(self, a, b):
        result = a + b
        op = f"{a} + {b} = {result}"
        self.history.append(op)
        return op

    def sub(self, a, b):
        result = a - b
        op = f"{a} - {b} = {result}"
        self.history.append(op)
        return op

    def multi(self, a, b):
        result = a * b
        op = f"{a} * {b} = {result}"
        self.history.append(op)
        return op

    def divide(self, a, b):
        result = a / b
        op = f"{a} / {b} = {result}"
        self.history.append(op)
        return op

    # Sin,Cos,Tan
    def sin(self, a):
        result = math.sin(a)
        op = f"{a} sin = {result} "
        self.history.append(op)
        return op

    def cos(self, a):
        result = math.cos(a)
        op = f"{a} cos = {result} "
        self.history.append(op)
        return op

    def tan(self, a):
        result = math.tan(a)
        op = f"{a} tan = {result} "
        self.history.append(op)
        return op

    # Power,SqRoot
    def root(self, a, b):
        # result = a**b
        result = math.pow(a, b)
        op = f"{a} root {b} = {result} "
        self.history.append(op)
        return op

    def sq_root(self, a):
        result = math.sqrt(a)
        op = f"Squre Root of {a} = {result} "
        self.history.append(op)
        return op

    # Natural , Common Log
    def nt_log(self, a):
        result = math.log(a)
        op = f"Natural log{a} = {result} "
        self.history.append(op)
        return op

    def cm_log(self, a):
        result = math.log(a, 10)
        op = f"Common log {a} = {result} "
        self.history.append(op)
        return op


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

Press 5 For Power
Press 6 For Squre Root

Press 7 For Sin
Press 8 For Cos
Press 9 For Tan

Press 10 For Natural Log
Press 11 For Common Log

      """
)

Choice = int(input("What is You Choise : "))

if Choice <= 5:

    num1 = int(input("Enter Frist Number : "))
    num2 = int(input("Enter Second Number : "))
else:
    num1 = int(input("Enter Frist Number : "))

if Choice == 1:
    result = calc.add(num1, num2)
    print(result)

elif Choice == 2:
    result = calc.sub(num1, num2)
    print(result)

elif Choice == 3:
    result = calc.multi(num1, num2)
    print(result)

elif Choice == 4:
    result = calc.divide(num1, num2)
    print(result)

elif Choice == 5:
    result = calc.root(num1, num2)
    print(result)

elif Choice == 6:
    result = calc.sq_root(num1)
    print(result)

elif Choice == 7:
    result = calc.sin(num1)
    print(result)

elif Choice == 8:
    result = calc.cos(num1)
    print(result)

elif Choice == 9:
    result = calc.tan(num1)
    print(result)

elif Choice == 10:
    result = calc.nt_log(num1)
    print(result)

elif Choice == 11:
    result = calc.cm_log(num1)
    print(result)

else:
    print("Invalid Choice")
