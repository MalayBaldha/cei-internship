# user input of a year
year = int(input())

# check for leap year
if year%100 == 0 and year%400 == 0: # condition where year is divisible by both 100 and 400
    print("Leap year.")
elif year%4 == 0 and year%100 != 0:                   # year divisible by 4 but not by 100
    print("Leap year.")
else:                               # non-leap year condition 
    print("Not a leap year.")