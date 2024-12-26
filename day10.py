with open("data/input10.txt") as f:
    inp=f.read().strip()
def descr(s):
    s=" "+s
    L=[]
    for i in range(1,len(s)):
        if s[i]!=s[i-1]:L.append(1);L.append(s[i])
        else:L[-2]+=1
    return "".join(str(x) for x in L)
for i in range(40):inp=descr(inp)
part1=len(inp)
for i in range(10):inp=descr(inp)
part2=len(inp)
print(part1,part2)