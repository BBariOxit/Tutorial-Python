#Input: s="abcaabbc"
#Output: {"a":3,"b":3,"c":2}
s = "abcaabbc"
freq = {}
for i in s:
    freq[i] = freq.get(i, 0) + 1 
print(freq)
# i = 'a'
# freq['a'] = freq.get('a', 0) + 1
# freq.get('a', 0) → 0 (vì 'a' chưa có trong freq)
# freq['a'] = 0 + 1 → freq['a'] = 1
# freq = {'a': 1}
# i = 'b'
# freq['b'] = freq.get('b', 0) + 1
# freq.get('b', 0) → 0 (vì 'b' chưa có trong freq)
# freq['b'] = 0 + 1 → freq['b'] = 1
# freq = {'a': 1, 'b': 1}
# i = 'c'
# freq['c'] = freq.get('c', 0) + 1
# freq.get('c', 0) → 0 (vì 'c' chưa có trong freq)
# freq['c'] = 0 + 1 → freq['c'] = 1
# freq = {'a': 1, 'b': 1, 'c': 1}
# i = 'a'
# freq['a'] = freq.get('a', 0) + 1
# freq.get('a', 0) → 1 (vì 'a' đã có trong freq với giá trị 1)
# freq['a'] = 1 + 1 → freq['a'] = 2
# freq = {'a': 2, 'b': 1, 'c': 1}
# i = 'a'
# freq['a'] = freq.get('a', 0) + 1
# freq.get('a', 0) → 2 (vì 'a' đã có trong freq với giá trị 2)
# freq['a'] = 2 + 1 → freq['a'] = 3
# freq = {'a': 3, 'b': 1, 'c': 1}
# i = 'b'
# freq['b'] = freq.get('b', 0) + 1
# freq.get('b', 0) → 1 (vì 'b' đã có trong freq với giá trị 1)
# freq['b'] = 1 + 1 → freq['b'] = 2
# freq = {'a': 3, 'b': 2, 'c': 1}
# i = 'b'
# freq['b'] = freq.get('b', 0) + 1
# freq.get('b', 0) → 2 (vì 'b' đã có trong freq với giá trị 2)
# freq['b'] = 2 + 1 → freq['b'] = 3
# freq = {'a': 3, 'b': 3, 'c': 1}
# i = 'c'
# freq['c'] = freq.get('c', 0) + 1
# freq.get('c', 0) → 1 (vì 'c' đã có trong freq với giá trị 1)
# freq['c'] = 1 + 1 → freq['c'] = 2
# freq = {'a': 3, 'b': 3, 'c': 2}
# Kết quả cuối cùng:
# {'a': 3, 'b': 3, 'c': 2}

# Sử dụng Counter từ collections
from collections import Counter
freq2 = Counter(s).most_common() 
print(freq2)

# sử dụng defaultdict từ collections
from collections import defaultdict
freq3 = defaultdict(int)
for i in s:
    freq3[i] += 1   
print(dict(freq3))
# defaultdict(int) → tạo defaultdict với giá trị mặc định là 0
# i = 'a'
# freq3['a'] += 1 → freq3['a'] = 0 + 1 = 1
# freq3 = {'a': 1}
# i = 'b'
# freq3['b'] += 1 → freq3['b'] = 0 + 1 = 1
# freq3 = {'a': 1, 'b': 1}
# i = 'c'
# freq3['c'] += 1 → freq3['c'] = 0 + 1 = 1
# freq3 = {'a': 1, 'b': 1, 'c': 1}
# i = 'a'
# freq3['a'] += 1 → freq3['a'] = 1 + 1 = 2
# freq3 = {'a': 2, 'b': 1, 'c': 1}
# i = 'a'
# freq3['a'] += 1 → freq3['a'] = 2 + 1 = 3
# freq3 = {'a': 3, 'b': 1, 'c': 1}
# i = 'b'
# freq3['b'] += 1 → freq3['b'] = 1 + 1 = 2
# freq3 = {'a': 3, 'b': 2, 'c': 1}
# i = 'b'
# freq3['b'] += 1 → freq3['b'] = 2 + 1 = 3
# freq3 = {'a': 3, 'b': 3, 'c': 1}
# i = 'c'
# freq3['c'] += 1 → freq3['c'] = 1 + 1 = 2
# freq3 = {'a': 3, 'b': 3, 'c': 2}
# Kết quả cuối cùng:
# {'a': 3, 'b': 3, 'c': 2}