#!/usr/bin/python3

# it retrieve an element from a list in C
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return
    return my_list[idx]
