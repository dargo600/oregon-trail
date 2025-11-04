#!/usr/bin/env python

""" Various Functions that are ported from BASIC """
#BASIC gen_zoning
#2040 PRINT "FOOD","BULLETS","CLOTHING","MISC. SUPP.","CASH"
# https://archive.org/details/bitsavers_cdccyberlaBASICOct80_41102953/page/n85/mode/2up
def gen_zoning(print_list: list) -> str:
    """
    Mimick gen_zoning function from BASIC
    """
    result : str = ""
    for item in print_list:
        padded_item = str(item).ljust(15)
        result.join(padded_item)
    result.join("\n")
    return result

# https://archive.org/details/bitsavers_cdccyberlaBASICOct80_41102953/page/n85/mode/2up?q=TAB
def tab(count) -> str:
    """
    Mimick TAB function from BASIC
    """
    return " " * count
