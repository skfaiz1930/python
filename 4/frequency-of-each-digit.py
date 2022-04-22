#  Write a Python program to find frequency of each digit in a given integer.

# Function which returns 
def frequency_calculator(x):
    freq = dict()   # Initialize a dictionary to keep the track of frequency of digits
    while(x):       # Loop until the number is not reduced
        unit_dig = x%10    # Get the last unit digit
        if (unit_dig in freq):    # If the key exists in dictionary, then increment the corresponding value for the key
            freq[unit_dig] = (freq[unit_dig] + 1) 
        else:
            freq[unit_dig] = 1    # If the key doesn't exist, initialize value for the corresponding key
        x = int(x/10)
    return freq
print(frequency_calculator(1343241234134234234))