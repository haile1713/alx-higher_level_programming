#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    count = 0
    if idx < 0 or idx > len(my_list):
        return my_list
    for i in my_list:
        if count == idx:
            my_list[idx] = element
        count += 1

    return my_list
