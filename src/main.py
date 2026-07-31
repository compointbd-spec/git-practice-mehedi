from datetime import date
from utils import add, subtract, multiply, divide

print("Name: Md. Mehedi Hasan")
print("Today's Date: ", date.today())

num1 = 10
num2 = 5

print("Addition: ", add(num1, num2))
print("Subtraction: ", subtract(num1, num2))
print("Multiplication: ", multiply(num1, num2))
print("Division:", divide(num1, num2))
print("Division by zero:", divide(num1, 0))