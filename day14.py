import re
from collections import Counter
with open("data/input14.txt") as f:
    pattern=r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds."
    data=[[int(x) for x in line[1:]] for line in re.findall(pattern,f.read())]

def dist(spd,dur,rest,t):
    q,r=t//(dur+rest),t%(dur+rest)
    return q*dur*spd+min(r,dur)*spd

scores=Counter()
for t in range(1,2504):
    L=[dist(spd,dur,rest,t) for spd,dur,rest in data]
    for i,x in enumerate(L):
        if x==max(L):
            scores[i]+=1
part1,part2=max(L),max(scores.values())
print(part1,part2)