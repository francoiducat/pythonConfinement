# Syntax Error
# print 3
# int 3
# Runtime Error
# a=2
# b="1"
# print(a+b)

a = 1
b = 0
try:
    z = a / b
    print(z)
except ZeroDivisionError:
    print("Cannot divide by 0")

x = (a / b) if b != 0 else "division by 0 WTF ?"
print(x)
