calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return (len(string), string.upper(),string.lower())
    
def is_contains(string, my_lst):
    count_calls()
    for i in my_lst:
        if string.lower() in i.lower():
            return True

# my_str = 'dimon'
# my_lst = ['123', 'mystr', 'dimon']
# string_info('dimon')
# print (is_contains(my_str, my_lst))
# print (is_contains('simon', [133, 'dimon', 'simon']))
# print (calls)

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)