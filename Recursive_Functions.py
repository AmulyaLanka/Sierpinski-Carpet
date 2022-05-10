# #sum all digits from 1 to a value
#
# def iterativeSum(n: int):
#     total = 0
#     for i in range(n+1):
#         total += i
#     return total
#
# def recursiveSum(n):
#     if n > 0:
#         return n + recursiveSum(n-1)
#     else:
#         return 0
#
#
# print(iterativeSum(10))
# print(recursiveSum(10))


# def showStack(n):
#     if n > 0:
#         print(f"putting {n} on the stack")
#         showStack(n-1)
#         print(f"taking {n} off the stack")
#
#
# showStack(5)

def count(n):
    if n > 0:
        count(n - 1)
        print(n)


count(10)