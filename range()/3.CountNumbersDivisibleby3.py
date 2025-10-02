# Count numbers divisible by 3 from 1 to 100
total = 0
for i in range(3,101):#range(3,101,3)
    if i % 3 == 0:
        total += 1
print(total)
#using len with range
print(len(list(range(3,101,3))))
#list comprehension
print(len([i for i in range(3,101) if i % 3 == 0]))
#filter()
print(len(list(filter(lambda x : x % 3 == 0, range(3,101)))))
#sum with generator expression
print(sum(1 for i in range(3,101) if i % 3 == 0))
#using step in range
print(sum(1 for _ in range(3,101,3)))
#using generator expression
print(sum(1 for i in range(3,101) if i % 3 == 0))
#using filter with generator expression
print(sum(1 for _ in filter(lambda x : x % 3 == 0, range(3,101))))
#using len with filter
print(len(list(filter(lambda x : x % 3 == 0, range(3,101)))))
#using list comprehension
print(len([i for i in range(3,101) if i % 3 == 0]))
#using sum with list comprehension
print(sum(1 for i in [i for i in range(3,101) if i % 3 == 0]))
#using sum with filter
print(sum(1 for _ in filter(lambda x : x % 3 == 0, range(3,101))))
#using len with generator expression
print(len(list(i for i in range(3,101) if i % 3 == 0)))
#using sum with range and step
print(sum(1 for _ in range(3,101,3)))
#using map
print(sum(map(lambda x : 1, filter(lambda x : x % 3 == 0, range(3,101)))))
#using reduce
from functools import reduce
print(reduce(lambda x, y: x + 1, filter(lambda x : x % 3 == 0, range(3,101)), 0))
#using reduce with map
print(reduce(lambda x, y: x + y, map(lambda x : 1, filter(lambda x : x % 3 == 0, range(3,101))), 0))
#using reduce with list comprehension
print(reduce(lambda x, y: x + 1, [i for i in range(3,101) if i % 3 == 0], 0))
#using reduce with generator expression
print(reduce(lambda x, y: x + 1, (i for i in range(3,101) if i % 3 == 0), 0))
#using reduce with range and step
print(reduce(lambda x, y: x + 1, range(3,101,3), 0))
#using len with map
print(len(list(map(lambda x : x, filter(lambda x : x % 3 == 0, range(3,101))))))
#using len with reduce
print(reduce(lambda x, y: x + 1, filter(lambda x : x % 3 == 0, range(3,101)), 0))
#using len with map and filter
print(len(list(map(lambda x : x, filter(lambda x : x % 3 == 0, range(3,101))))))
#using len with reduce and filter
print(reduce(lambda x, y: x + 1, filter(lambda x : x % 3 == 0, range(3,101)), 0))
