# Nested Functions calls = function calls inside other functions calls
#                          innermost function calls are resolved first
#                          returned value is used as argument for the
#                          next outer function.

# num = input('Enter a whole positive number: ')
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

# Nested functions calls
# print(
#     round(
#         abs(
#             float(
#                 input("Enter a whole positive number: ")
#             )
#         )
#     )
# )

# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amout of arguments


def add(*nums):
    sum = 0
    nums = list(nums)
    nums[0] = 23
    for i in nums:
        sum += i
    return sum


print(add(1, 2, 3, 4, 5, 6))
