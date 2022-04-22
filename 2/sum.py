# Write a Python program to find sum of all natural numbers between 1 to n.

number = int(input("Please Enter any Number: "))
i = 1
sum = 0


while ( i <= number):
    sum = sum + i
    i = i + 1
    
print("The Sum is {0}".format(sum))
