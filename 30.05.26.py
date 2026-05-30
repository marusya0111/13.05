#1задача
# def max_area(height):
#     l = 0
#     r = len(height)-1
#     max_water = 0
#     while l < r:
#         current = (r - l) * min(height[l],height[r])
#         max_water = max(current, max_water)
#         if height[r] < height[l]:
#             r = r - 1
#         else:
#             l = l + 1
#     return max_water
# height = [1,8,6,2,5,4,8,3,7]
# print(max_area(height))

#2
# Дан список целых чисел nums, отсортированный по неубыванию.
# Верните список квадратов всех чисел, тоже отсортированный по неубыванию.
# Требуемая сложность: O(n)

# nums = [-4,-1,0,3,10]
# opa = []
# for i in nums:
#     v = i**2
#     opa.append(v)
#     s = sorted(opa)
# print(s)

#3
#Дан массив положительных целых чисел nums и целое число target.
# Найдите самую короткую непрерывную подпоследовательность (подмассив),
# сумма элементов которой ≥ target, и верните её длину.
# Если такой подмассив не существует — верните 0.
# Требуемая сложность: O(n)
# Ввод:
# nums = [2,3,1,2,4,3]
# target = 7
# Вывод:
# 2

nums = [1,4,4]
target = 4
def funcy(nums,target):
    l = 0
    min_lenght = 1000000
    summ = 0
    for r in range(len(nums)):
        summ+= nums[r]
        while summ >= target and l<= r:
            min_lenght = min(min_lenght, r - l + 1)
            summ -= nums[l]
            l+=1
    return min_lenght if min_lenght !=1000000  else 0
print(funcy(nums,target))