#Program to print Left Half Pyramid
k = 1
for i in range(0, 5):
    for j in range(0, k):
        print("* ", end="")
    k = k + 1
    print()
    