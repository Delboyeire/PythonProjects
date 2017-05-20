"""this is the nested.py module which contains one function
called print_lol which print lists which may or may contain nested lists"""


def print_lol(the_list,indent=false, level=0):
    """This function takes a positional argument called “the_list", which is any
    Python list (of, possibly, nested lists). Each data item in the provided list
    is (recursively) printed to the screen on its own line.A second arguement called 
    level is used to insert tab stops when a nested list is encountered """
    for item in the_list:
        if isinstance(item, list):
            print_lol(item, indent, level+1)
        else:
            if indent:
                print("\t" * level, end='')
            print(item)
