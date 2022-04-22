# 13. Write a Python program to swap first and last digits of a number.

def swap(num):
    str_num = str(num)
    str_swapped = str_num[-1] + str_num[1:-1] + str_num[0]
    return int(str_swapped)

print(swap(234))
