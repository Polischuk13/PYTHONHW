
 # 16 ЗАДАЧА
# def count_occurrences(arr, x):
#  count = 0
#  for num in arr:
#     if num == x:
#         count += 1
#  return count

# # Считываем количество элементов в массиве
# n = int(input())

# # Считываем элементы массива
# arr = list(map(int, input().split()))

# # Считываем число X
# x = int(input())

# # Вызываем функцию для подсчета вхождений числа X
# occurrences = count_occurrences(arr, x)

# # Выводим результат
# print(occurrences)

# 18 ЗАДАЧА
# def find_closest(arr, x):
#     closest_num = arr[0]
#     min_diff = abs(x - arr[0])
#     for num in arr:
#         diff = abs(x - num)
#         if diff < min_diff:
#             min_diff = diff
#             closest_num = num
#     return closest_num

# # Считываем количество элементов в массиве
# n = int(input())

# # Считываем элементы массива
# arr = list(map(int, input().split()))

# # Считываем число X
# x = int(input())

# # Вызываем функцию для поиска ближайшего элемента
# closest = find_closest(arr, x)

# # Выводим результат
# print(closest)