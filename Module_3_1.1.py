calls = 0


def count_calls():
    global calls
    calls = calls +1
    return calls

    
    count_calls()


def string_info(*args):
    global calls
    calls = calls + 1
    print(args)
    # print(count_calls())
    count_calls()
string_info('Capybara'.upper(), 'Capybara'.lower(), len('Capybara'))
string_info('Armagedon'.upper(), 'Armagedon'.lower(), len('Armagedon'))


def is_contains(string, list_to_search):
    if string in list_to_search:
        print(True)
    else:
        print(False)
        global calls
        calls = calls + 1
    print(string, list_to_search)
    count_calls()

is_contains('Urban', ['ban', 'BaNaN', 'Urban'])
is_contains('cycle', ['recycling', 'cyclic'])
