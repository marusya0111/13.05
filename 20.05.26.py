# from time import time
#
# start = time()
# for i in range(10):
#     print(123)
# end = time()
# print(end-start)

#import timeit
# from timeit import timeit
# s = """
# for i in range (100):
#     print(i)
# """
#
# def a (num1,num2):
#     z = num1+ num2
#     z1 = num1 - num2
#     return z *z1
#
# time_result = timeit(
#     stmt = "a(num1,num2)", # код который будет замеряться по времени
#     number = 90,
#     setup = "num1,num2 = 10000,200",
#     globals = globals()
# )
# print(time_result/90)


# s = "hello wolrd"
# s.replace("l","&")
# table = {
#     ord("l"): ord("&"),
#     ord("o"): ord("@"),
#     ord("h"): None
# }
# table = str.maketrans("lo","&@","h")
# table = str.maketrans({
#      "l":"&",
#      "o": "@",
#      "h": None
# })
# res = s.translate(table)
# print(res)

# #1
# from timeit import timeit
# code1 = """
# s = "a"
# for i in range(1000):
#     s+="a"
# """
# code2 = """
# k = "".join(["a" for _ in range(1000)])
# """
# program1 = timeit(code1,number = 10000)
# program2 = timeit(code2,number = 10000)
# print(program1,program2)

#2
# from timeit import timeit
# a = list(range(1000))
# code1 = """
# sum_num = sum(a)
# """
#
# code2 = """
# sum_num = 0
# for i in a:
#     sum_num += i
# """
# program1 = timeit(code1,number = 1000,globals =globals())
# program2 = timeit(code2,number = 1000,globals =globals())
# print(program2/program1)

#3
#s.sort sourted(s)
from random import randint
from timeit import timeit

s = [randint(1,10_000) for _ in range(10_000)]

s = []
for _ in range(10_000):
    a = randint(1,10_000)
    s.append(a)

code1 = """s.sort()
"""
s = [randint(1,10_000) for _ in range(10_000)]


code2 = """
k = "sorted(s)
"""
program1 = timeit(code1,number = 1000,globals =globals())
program2 = timeit(code2,number = 1000,globals =globals())
print(program2/program1)
#sort быстрее
