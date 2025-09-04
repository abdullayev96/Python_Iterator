#############################   Iterator

# nums = [10, 20, 30]
# it = iter(nums)      # iterator obyektini yaratamiz
#
# print(next(it))      # 10
# print(next(it))      # 20
# print(next(it))      # 30
# print(next(it))      # StopIteration (endi element qolmadi)





################  for bilan


# for i in nums:
#     print(i)



####################################   5 DAN 20 GACHA TOQ SONLARNI OLISH

# class MyRange:
#     def __init__(self, start, end):
#         self.current = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current >= self.end:
#             raise StopIteration
#         val = self.current
#         self.current += 1
#         return val
#
#
# for num in MyRange(5, 10):
#     print(num)


# n = int(input("N son:"))
#
# for i in range(n, 20):
#     if i%2 == 1:
#         print(i)


##################   1 mlrd  sonlarni chiqarmoqchi bolsak


# numbers = [i for i in range(1, 1_000_000_000) if i % 2 == 1]
# print(numbers)


########################    Iteratorni foydasi

# class OddRange:
#     def __init__(self, start, end):
#         self.current = start if start % 2 == 1 else start + 1
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current >= self.end:
#             raise StopIteration
#         val = self.current
#         self.current += 2
#         return val
#
# for num in OddRange(1, 1_000_000_000):
#     if num > 100000:
#         break
#     print(num)



###############   Faqat juft sonlar qaytarish

# for i in range(2, 10000000):     ###########   Oddiy range bilan
#     if i%2 == 0:
#         print(i)


# class EvenNumbers:                           #############  Iterator bilan
#     def __init__(self, start, end):
#         self.current = start if start % 2 == 0 else start + 1
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current >= self.end:
#             raise StopIteration
#         val = self.current
#         self.current += 2
#         return val
#
# for i in EvenNumbers(2, 10000000):
#     print(i)


############   max songacha chiqarish


# class CountUpTo:
#     def __init__(self, max):
#         self.max = max
#         self.current = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current > self.max:
#             raise StopIteration
#         val = self.current
#         self.current += 1
#
#         return val
#
# for i in CountUpTo(5):
#     print(i)


#
# def my_gen():
#     print("Started")
#     yield "Hello"
#     print("Continuing")
#     yield "World"
#
# for i in my_gen():
#     print(i)

# g = hello_gen()
# print(next(g))  # 'Started' chiqadi, keyin 'Hello'
# print(next(g))


### 1
##print(oct(23))

### 2

#print(~(~4))

### 3

print("10 > 5 and 5 < 3")