# Input: n=10
# Output: {1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64,9:81,10:100}
n = 10
result = {i: i**2 for i in range(1,n +1)} 
print(result)
# using dict and zip
result2 = dict(zip(range(1,n +1), (i**2 for i in range(1,n +1))))
print(result2)