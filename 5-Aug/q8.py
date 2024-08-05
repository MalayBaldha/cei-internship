# print numbers from 1-10 not divisible by 3

for i in range(1,11):
    if i%3 == 0:
        continue    #using continue for divisibility condition
    print(i)