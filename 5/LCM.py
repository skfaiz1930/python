

if(3 > 7):
    maximum = 3
else:
    maximum = 7

while(True):
    if(maximum % 3 == 0 and maximum % 7 == 0):
        print("\n Least Common Multiple of {0} and {1} = {2}".format(3, 7, maximum))
        break;
    maximum = maximum + 1
    