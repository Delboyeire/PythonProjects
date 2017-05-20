'''this is the nested.py module which contains one function
called print_lol which print lists which may or may contain nested lists'''
def print_lol(the_list):
    '''This function takes a positional argument called “the_list", which is any
    Python list (of, possibly, nested lists). Each data item in the provided list
    is (recursively) printed to the screen on its own line.'''   
    for item in the_list:
        if isinstance(item, list):
            print_lol(item)
        else:
            print(item)
            
