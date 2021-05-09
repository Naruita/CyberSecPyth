from itertools import accumulate, takewhile

numbers = (list(accumulate(range(8))))
print(numbers)
print(list(takewhile(lambda x: x <= 10, numbers)))