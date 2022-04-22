# Write a Python program to print all natural numbers in reverse (from n to 1).


number = int(input("Please Enter any Number: "))
i = 1

print("The Reverse of Natural Numbers from {0} to 1 are".format(number)) 

while ( number >= i):
    print (number, end = '  ')
    number = number - 1