calls = 0

def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string):         # Вывод информации о строке
    print(string.upper())
    print(string.lower())
    print(len(string))
    count_calls()                # Увеличиваем счётчик вызовов


string_info('Capybara')         # Вызов функции с строками
string_info('Armagedon')

def is_contains(string, list_to_search):
    if string in list_to_search:
        print(True)
    else:
        print(False)
    print(string, list_to_search)
    count_calls()                            # Увеличиваем счётчик вызовов


is_contains('Urban', ['ban', 'BaNaN', 'Urban'])  # Вызовы функции
is_contains('cycle', ['recycling', 'cyclic'])


print(f'Функция count_calls вызвана {calls} раза.')                  # Вывод количества вызовов