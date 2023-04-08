# Intro to python list comprehension

# sourcery skip: for-append-to-extend, for-index-underscore, list-comprehension
nums = [1, 2, 3]
print([i * 2 for i in nums])  # it times 2 for every number in the list
nums_square = [i * 2 for i in nums]

nums = [1, 2, 3, 4, 5, 6]

results = []

for i in nums:
    i *= 2
    print('i', i)
    results.append(i)

# List comprehension litrelary does the above

nums = [item * 3 for item in nums]
print('Results', results)

print(nums)


strings = ['intro', 'to', 'list', 'comprehension']

restults_strings = [word.upper() for word in strings]  # Made by myself hehe

# The line above does the same thing as:
results_test_string = []

for word in strings:
    results_test_string.append(word.upper())

print('Results', restults_strings)
print('Results 2:', results_test_string)


# The key feature for a list comprehesion is that uses list
# [expression for item in iterable]:

# Can also be used with strings or any iterable (Self test)
string = 'Alo'
list_comprehension_xemple = [item.upper() for item in string]
print(list_comprehension_xemple)
# ^
# |
# Expression


# The iterable can be set in the list comprehension itself:

list_comprehension_xemple = [item * 2 for item in [1, 2, 3]]
print(list_comprehension_xemple)


def timesFive(number):
    return number * 5


# sourcery skip: for-append-to-extend, list-comprehension
numbers_for_timesFive = [1, 2, 3, 4, 5, 6]

results_timesFive = []

for item in numbers_for_timesFive:
    i = timesFive(item)
    print(i)
    results_timesFive.append(i)

print('Results with function', results_timesFive)

# Using function inside list comprehension
results_with_listcomprehension = [
    timesFive(number) for number in numbers_for_timesFive
]

print('Results with list comprehension', results_with_listcomprehension)

dictionarys = [
    {'name': 'Augusto'},
    {'name': 'Nicoly'},
]
results_dict = []
for dictionary in dictionarys:
    results_dict.append(dictionary['name'])

print(results_dict)

results_dict_list_comprehension = [
    dictionary['name'] for dictionary in dictionarys
]
print(results_dict_list_comprehension)