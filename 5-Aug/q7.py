# print multiplication table for a given input number using while loop

number = int(input())

counter = 1 # counter for loop

#initiating while loop
while counter < 11:
    print(f"{number} x {counter} = {number*counter}")
    counter += 1    #increment counter