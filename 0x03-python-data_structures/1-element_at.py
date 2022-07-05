#!/usr/bin/python3
def element_at(my_list, idx):
    count = 0
    if idx > len(my_list) or idx < 0:
        return None
    for i in my_list:
        if count == idx:
            return i
        count += 1
