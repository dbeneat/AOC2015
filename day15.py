import re
from collections import Counter
with open("data/input15.txt") as f:
    pattern=r"capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)"
    data=[[int(x) for x in line] for line in re.findall(pattern,f.read())]

part1,part2=0,0
for a in range(1,101):
    for b in range(1,101-a):
        for c in range(1,101-a-b):
            for d in range(1,101-a-b-c):
                score=1
                for i in range(4):
                    n=a*data[0][i]+b*data[1][i]+c*data[2][i]+d*data[3][i]
                    if n>0: score*=n
                cal=a*data[0][4]+b*data[1][4]+c*data[2][4]+d*data[3][4]
                if score>part1: part1=score
                if score>part2 and cal==500: part2=score
print(part1,part2)