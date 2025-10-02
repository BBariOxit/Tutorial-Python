# Sum numbers from 0 to 100
total = 0
for i in range(101):
    total += i
print(total)
#using sum with range
print(sum(range(101)))
#using sum with generator expression
print(sum(i for i in range(101)))
#using sum with list comprehension
print(sum([i for i in range(101)]))
#using sum with filter
print(sum(filter(lambda x : True, range(101))))
#using sum with map
print(sum(map(lambda x : x, range(101))))
#using sum with reduce
from functools import reduce
print(reduce(lambda x, y: x + y, range(101)))


