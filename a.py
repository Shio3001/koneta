s = str(334**334)
#s = str(334*334)

t = 334
for i in range(333):
    t = t * 334
    print(t)

print(s)

if s == str(t):
    print("一致")
else:
    print("不一致")

if "334" in s:
    print("aho")

print(s.find("334"))

for i , k in enumerate(s):
    print(i,k)