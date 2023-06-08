# def power(a, b):

#     if b == 0:
#         return 1
#     elif b % 2 == 0:
#         return power(a*a, b/2)
#     else:
#         return a * power(a, b-1)

# A = int(input("Введите число A: "))
# B = int(input("Введите степень B: "))

# print(A, "^", B, "=", power(A, B)) 


# def sum(a, b):
#     if b == 0:
#         return a
#     else:
#         return sum(a ^ b, (a & b) << 1)

# a = int(input())
# b = int(input())
# print(sum(a, b)) 