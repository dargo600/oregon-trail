#!/usr/bin/env python

#BASIC print_zoning
#2040 PRINT "FOOD","BULLETS","CLOTHING","MISC. SUPP.","CASH"
# https://archive.org/details/bitsavers_cdccyberlaBASICOct80_41102953/page/n85/mode/2up
def print_zoning(print_list):
    """
    Mimick print_zoning function from BASIC
    """
    for item in print_list:
        padded_item = str(item).ljust(15)
        print(f"{padded_item}", end="")
    print("")

# 
#https://archive.org/details/bitsavers_cdccyberlaBASICOct80_41102953/page/n85/mode/2up?q=TAB
def tab(count):
    """
    Mimick TAB function from BASIC 
    """
    return " " * count

def get_user_input(prompt, min_value, max_value):
    """
    Check value and prompt for a new value if not in between the min/max value
    """
    while True:
        val = int(input(prompt))
        if min_value <= val and val <= max_value:
            break
        print(f"INVALID INPUT.  PLEASE ENTER A VALUE BETWEEN {min_value} and {max_value}\n")
    return val

