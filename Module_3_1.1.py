calls = 0

def count_calls():
    global calls
    calls = calls + 1

print(calls)
count_calls()


def string_info(*args):
    def count_calls():
          global calls      
          calls = calls + 1 
    print(args)
    print(calls)
string_info('Capybara'.upper(), 'Capybara'.lower(), len('Capybara'))
string_info('Armagedon'.upper(), 'Armagedon'.lower(), len('Armagedon'))
count_calls()



def is_contains(string, list_to_search):
    def count_calls():
        global calls
        calls = calls + 1
    if string in list_to_search:
        print(True)
    else:
        print(False)
    print(string, list_to_search)
    print(calls)

is_contains('Urban', ['ban', 'BaNaN', 'Urban'])
is_contains('cycle', ['recycling', 'cyclic'])
count_calls()