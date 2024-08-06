# define a function to add elements to array
def add_elements(array, *args):
    for i in args[0]:
        array.append(int(i))
    return array


# python list
lst = [21,43,54,66,32]

print(lst)

# input elements and add them to array
lst = add_elements(lst, input().split())

print(lst)