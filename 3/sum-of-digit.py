# 14. Write a Python program to calculate sum of digits of a number.

def getSum(n):
    
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum
   
n = 12345
print(getSum(n))
