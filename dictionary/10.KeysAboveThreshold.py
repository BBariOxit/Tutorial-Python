# Input: d={"a":1,"b":6,"c":4,"d":9}; threshold=5
# Output: ["b","d"]
d = {"a": 1, "b": 6,"c": 4,"d": 9}
threshold = 5
result = {k for k,v in d.items() if v > threshold}
print(result)