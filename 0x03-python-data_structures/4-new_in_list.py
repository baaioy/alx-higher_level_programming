#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if not my_list:
        pass
    else:
        new_list = my_list[:]
        if idx < 0:
            return new_list
        if idx > len(my_list) - 1:
            return new_list
        new_list[idx] = element
        return new_list
