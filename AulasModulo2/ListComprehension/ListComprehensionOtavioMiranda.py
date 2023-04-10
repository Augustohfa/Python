def divide(x, y):
    return x / y


nums = [1, 2, 3, 4, 5]

print(nums)
# print(new_nums)

# new_nums_comprehension = [num for num in nums]

# print(new_nums_comprehension)

# # Mesma coisa com FOR

# new_nums_for = []

# for nums in nums:
#     new_nums_for.append(nums)

# print(new_nums_for)

"""
Porque usar list comprehension?
Em alguns casos quando da pra fazer algo do for
com menos linhas
"""

divide_by_2 = [num / 2 for num in nums]
print(divide_by_2)

double = [num * 2 for num in nums]
print(double)

divided = [divide(num, 2) for num in nums]
print(divided)


new_nums = range(1, 11)

nums_in_comprehension_filter = [num for num in new_nums if num >= 5]
print(nums_in_comprehension_filter)

odd_numbers = [num for num in new_nums if num % 2 != 0]
pair_numbers = [num for num in new_nums if num % 2 != 0]

print(odd_numbers, '\n', pair_numbers)
