from collections import defaultdict
from itertools import permutations
with open("data/input13.txt") as f:
    L=f.read().strip().split("\n")
guests=set()
energy=defaultdict(int)
for line in L:
    line=line.split()
    a,b,c,d=line[0],line[2],int(line[3]),line[10][:-1]
    guests.add(a)
    if b=="lose":c*=-1
    energy[(a,d)]=c

def total(conf):
    r=0
    for i in range(len(conf)-1):
        r+=energy[(conf[i],conf[i+1])]
        r+=energy[(conf[i+1],conf[i])]
    r+=energy[(conf[-1],conf[0])]
    r+=energy[(conf[0],conf[-1])]
    return r

part1=max(total(conf) for conf in permutations(guests))
part2=max(total(conf) for conf in permutations(guests|{"me"}))
print(part1,part2)