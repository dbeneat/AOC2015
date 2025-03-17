from collections import Counter
c=Counter()
def partitions(n,nbcontainers,lst):
    if len(lst)==0:
        if n==0: c[nbcontainers]+=1
        return
    partitions(n,nbcontainers,lst[1:])
    if lst[0]<=n: partitions(n-lst[0],nbcontainers+1,lst[1:])

with open("data/input17.txt") as f:
    L=[int(x) for x in f.read().strip().split("\n")]

partitions(150,0,L)
part1,part2=sum(c.values()),c[min(c)]
print(part1,part2)