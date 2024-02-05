#!/usr/bin/python3
def safe_print_list(my_list=None, x=0):
    if my_list is None:
        my_list = []

    n = 0
    for m in range(x):
        try:
            print(my_list[m], end="")
            n += 1
        except IndexError:
            break
    print()
    return n
