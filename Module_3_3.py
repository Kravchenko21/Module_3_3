def print_params(a=1, b='строка', c=True):
    print(a,b,c)

print_params()
print_params(a=2, b=3, c=4)
print_params(b = 25)
print_params(c = [1,2,3])


values_list_2 = [2, 'Eva']
values_list = [15, 'Mery', False]
values_dict = {'a': 'Pavel', 'b': 1995, 'c': True}
def print_params(a=1, b='строка', c=True):
    print(a,b,c)
    global values_list_2
    global values_list
    global values_dict
    print_params = values_list
    print_params = values_dict
    print_params = values_list_2

print()
print_params(*values_list)
print_params(*values_list_2, 42)
print_params(**values_dict)