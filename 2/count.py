# Write a Python program to count number of digits in a number.


Number = int(input("Please Enter any Number: "))
Count = 0
while(Number > 0):
    Number = Number // 10
    Count = Count + 1

print("Number of Digits in a Given Number = %d" %Count)