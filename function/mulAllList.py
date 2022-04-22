def mul(numbers):
    prod = 1
    for x in numbers:
        prod *= x
    return prod

print(mul([1, 2, 3, 4, 5]))
