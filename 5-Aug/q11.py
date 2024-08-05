# fucntion takes 2 arguments and returns their sum

def sum(x,y):
    return x + y

# calling sum()
n1, n2 = map(int, input().split())          #input both numbers in single line
print("Sum of numbers is :", sum(n1,n2))