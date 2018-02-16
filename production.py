import math

def return_square(alist, x):
    square_list = []
    for each in alist:
            square_list.append(math.pow(each, x))
    return square_list
