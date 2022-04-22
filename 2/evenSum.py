# Write a Python program to find sum of all even numbers between 1 to n.

num = int(input(" Please Enter any Maximum Number : "))
sum = 0
for number in range(1, num + 1):
    if(number % 2 == 0):
        sum = sum + number
     
     
     
print("The sum of even number is {0}".format(sum))