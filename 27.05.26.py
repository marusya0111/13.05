# 3.
# Есть длинная строка. Нужно узнать, сколько раз встречается "ab" тремя способами:
#
# count()
#
# Цикл с проверкой среза
#
# Разбиение через split()

# from timeit import timeit
#
# s = "aboewfjowejfiewjfeowkfodsabfokfopewow[ewfacefefew2222222223dfffdb"
#
# def count_func():
#     s.count("ab")
#
# def for_func():
#     count = 0
#     for i in range(len(s)):
#         if s[i:i +2] == "ab":
#             count+=1
#
# def split_func():
#     len(s.split("ab"))
#
# timer1 =timeit(stmt = "count_func()",number = 100, globals = globals())
# timer2 =timeit(stmt = "for_func()",number = 100, globals = globals())
# timer3 =timeit(stmt = "split_func()",number = 100, globals = globals())
#
# print(timer1,timer2,timer3)

#4
# from timeit import timeit
# stroka = str(list(range(200_000)) + list("abcde"))
#
# def func_in():
#     "abcde" in stroka
#
# def func_find():
#     stroka.find("abcde")
#
# def three():
#     return(len(stroka.split("abcde")) > 1)
#
# def four():
#     for i in range(len(stroka)):
#         if stroka[i:i + 5] == "abcde":
#                  return True
# timer1 =timeit(stmt = "func_in()",number = 100, globals = globals())
# timer2 =timeit(stmt = "func_find()",number = 100, globals = globals())
# timer3 =timeit(stmt = "three()",number = 100, globals = globals())
# timer4 =timeit(stmt = "four()",number = 100, globals = globals())
# print(timer1,timer2,timer3,timer4)


#5
nums = [1,2,3,4,5,6,7,8,9]
for i, target in enumerate(nums):
    if target ==5:
        print(i)

def find_target(nums,target):
    l = 0
    r = len(nums)-1
    while l <= r:
        m = (l+r)//2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m + 1
        else:
            r = m - 1
    return -1
print(find_target(nums,5))