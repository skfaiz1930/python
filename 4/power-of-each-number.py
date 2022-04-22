# Python Program to Find Power of a Number using For loop
b, x, i, r = None, None, None, 1

# b - To store base number
# x - To store exponent number
# r - To store result value

print ("-----Enter the input of base number-----")
b = int (input ())

print ("\n-----Enter the input of exponent number-----")
x = int (input ())

for i in range (x, 0, -1):
	r *= b

print ("\nThe calculation of the power of N number is ", b, "^", x, " = ", r)