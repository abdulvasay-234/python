# creating a calculator app which adds, subtracts, multiplies and divides two numbers
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1 + self.num2
    def subtract(self):
        return self.num1 - self.num2
    def multiply(self):
        return self.num1 * self.num2
    def divide(self):
        return self.num1 / self.num2
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
obj = Calculator(num1, num2)
print("Select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")
select = int(input("Select operations form 1, 2, 3, 4 :"))
if select == 1:
    print(num1, "+", num2, "=",
                    obj.add())
elif select == 2:
    print(num1, "-", num2, "=",
                    obj.subtract())
elif select == 3:
    print(num1, "*", num2, "=",
                    obj.multiply())
elif select == 4:
    print(num1, "/", num2, "=",
                    obj.divide())
else:
    print("Invalid input")
    