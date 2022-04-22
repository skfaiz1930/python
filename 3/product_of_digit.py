# 15. Write a Python program to calculate product of digits of a number.

def prod(n):
    
    sum = 1
    for digit in str(n): 
      sum *= int(digit)      
    return sum
   
n = 12345
print(prod(n))
