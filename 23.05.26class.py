#3dz
# from timeit import timeit
# from math import *
#
# def while_func(n):
#     if n <1 :
#         return False
#     if n <= 3:
#         return True
#     i = 4
#     while n >= i:
#         if n % i != 0:
#             i+=1
#         else:
#             return False
#
# def for_func(n):
#     if n < 1:
#         return False
#     for i in range(3,int(sqrt(n)+1),2):
#         if n% i == 0:
#             return False
#     return True
#
# def for_int_func(n):
#     if n <1 :
#         return False
#     for i in range (3,int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True
#
#
#
# program1 = timeit("for i in range (10_000): while_func(i)",number = 1,globals =globals())
# program2 = timeit("for i in range (10_000): for_func(i)",number = 1,globals =globals())
# program3 = timeit("for i in range (10_000): for_int_func(i)",number = 1,globals =globals())
#
# print(program1,program2,program3)

#2задача
# from timeit import timeit
# setup ="""
# a_list = list(range(1000_000))
# b_set = set(range(1000_000))
# """
# def list_func(n):
#     return int("9"*6 in a)
# def set_func(n):
#     return 999999 in b

# timer1 = timeit(stmt = "99999 in a_list", number=10000, setup = setup)
# timer2 = timeit(stmt = "99999 in b_list", number = 10000, setup = setup)
# print(timer1,timer2)

#3
# from random import randint
# from timeit import timeit
# nums = [randint(1,10_000) for _ in range(1,10_000)]
#
# def dublicates_loops(nums):
#     dubs = []
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i] == nums[j] and nums[i] not in dubs:
#                 dubs.append(nums[i])
#     return dubs
# def dublicates_set(nums):
#     dubs = set({})
#     seen = set({})
#     for i in range(len(nums)):
#         if nums[i] not in dubs:
#             dubs.add(nums[i])
#         else:
#             seen.add(nums[i])
#
# timer1 =timeit(stmt = "dublicates_loops(nums)",number = 10, globals = globals())
# timer2 = timeit(stmt = "dublicates_set(nums)", number = 10, globals = globals())
# print(timer1,timer2)

#4
# from timeit import timeit
# listy = list(range(10_000))
#
# def crez_func(listy):
#     return listy[::-1]
#
# def reversed_func(listy):
#     return reversed(listy)
#
# def reverse_func(listy):
#     return listy.copy.reverse()
#
# def for_func(listy):
#     s = []
#     for i in range (len(listy)-1,-1,-1):
#         s.append(listy[i])
#     return s
#
#
# timer1 =timeit(stmt = "crez_func(listy)",number = 10, globals = globals())
# timer2 = timeit(stmt = "reversed_func(listy)", number = 10, globals = globals())
# timer3 = timeit(stmt = "reverse_func(listy)", number = 10, globals = globals())
# timer4 = timeit(stmt = "for_func(listy)", number = 10, globals = globals())
# print(timer1,timer2,timer3,timer4)

