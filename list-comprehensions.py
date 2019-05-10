nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# we want n for each n in nums

# my_list = []
# for n in nums:
#     my_list.append(n)
# print(my_list)

# my_list = [n for n in nums]
# print(my_list)

# want n*n for each n in nums

# my_list = []
# for n in nums:
#     my_list.append(n * n)
# print(my_list)

# my_list = [n * n for n in nums]
# print(my_list)

# using a map + lambda    -----------this doesn't work in python 3+
# my_list = map(lambda n: n * n, nums)
# print(my_list)

# i want n for each n in nums if n is even
# my_list = []
# for n in nums:
#     if n % 2 == 0:
#         my_list.append(n)
# print(my_list)
