#How to Remove Letters From a String in Python
#cach1:replace()
s = "hello world"
New = s.replace("world", "Universe")
print(New)
#cach2:
new2 =""
for i in s:
    if i != "o":
        new2 += i 
print(new2)
#cach3:list compehension
new3 = "".join([i for i in s if i != "o"])
print(new3)
#cach4:filter()
new4 = "".join(filter(lambda i: i != "o", s))
print(new4)
#cach5:slicing
idx = s.find("o")
if idx != -1:
    new5 = s[:idx] + s[idx+1:]
print(new5)
