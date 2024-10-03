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
        if a == 0 or b == 0:
            return "Error : Cannot divide by Zero. "
        result = a / b
        op = f"{a} / {b} = {result}"
        self.history.append(op)
        return op

    def percent(self, part, total):
        if total == 0:
            return "Error : Cannot calculate percentage with Zero as the whole. "

        result = (part / total) * 100
        op = f"The percentage of {part} out of {total} is {result:.2f}%."
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
    def power(self, a, b):
        # result = a**b
        result = math.pow(a, b)
        op = f"{a} raised to the power of {b} = {result} "
        self.history.append(op)
        return op

    def sq_root(self, a):
        result = math.sqrt(a)
        op = f"Square Root of {a} = {result} "
        self.history.append(op)
        return op

    # Natural , Common Log
    def nt_log(self, a):
        if a < 0:
            return "Error: Cannot calculate square root of a negative number."

        result = math.log(a)
        op = f"Natural log{a} = {result} "
        self.history.append(op)
        return op

    def cm_log(self, a):
        result = math.log(a, 10)
        op = f"Common log {a} = {result} "
        self.history.append(op)
        return op

    def pi(self, a):
        result = math.pi * a
        op = f"Pi Value of {a}  = {result} "
        self.history.append(op)
        return op

    def inv(self, a):
        if a < 0:
            return "Error: Cannot calculate square root of a negative number."

        result = 1 / a
        op = f"Inverse of {a}  = {result} "
        self.history.append(op)
        return op

    def e(self, a):
        result = math.e * a
        op = f"Euler's number of {a}  = {result} "
        self.history.append(op)
        return op


calc = Calculator()
# print(calc.add(20, 10))
# print(calc.sub(20, 10))
# print(calc.multi(5, 5))
# print(calc.divide(50, 5))

# print(calc.history)

print("\nThis Is Basic Calculator ")
print("Which Operation Do you want to Perform ? Choose From Below Option :")
print(
    """
Please select an operation by pressing the corresponding number:

1. Addition (+)
2. Subtraction (−)
3. Multiplication (×)
4. Division (÷)

5. Power (^)
6. Square Root (√)

7. Sine (sin)
8. Cosine (cos)
9. Tangent (tan)

10. Natural Logarithm (ln)
11. Common Logarithm (log)

12. Pi (π)
13. Percentage (%)
14. Inverse (1/x)
15. Euler's number (e)
      """
)

Choice = int(input("What is You Choice : "))

if Choice in [1, 2, 3, 4, 5]:

    num1 = float(input("Enter First Number : "))
    num2 = float(input("Enter Second Number : "))

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
        result = calc.power(num1, num2)
        print(result)

elif Choice in [6, 7, 8, 9, 10, 11, 12]:
    num1 = float(input("Enter  Number : "))

    if Choice == 6:
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

    elif Choice == 12:
        result = calc.pi(num1)
        print(result)

    elif Choice == 14:
        result = calc.inv(num1)
        print(result)

    elif Choice == 15:
        result = calc.e(num1)
        print(result)


elif Choice == 13:
    num1 = float(input("Enter the whole (the total amount): "))
    num2 = float(
        input("Enter the part (the amount you want to find the percentage of): ")
    )
    if Choice == 13:
        result = calc.percent(num1, num2)
        print(result)

else:
    print("Invalid Choice")
