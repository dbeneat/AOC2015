from collections import defaultdict
with open("data/input09.txt") as f:
    L=f.read().strip().split("\n")
adj=defaultdict(list)
cities=set()
for row in L:
    a,b,c,d,e=row.split()
    adj[a].append((c,int(e)));adj[c].append((a,int(e)))
    cities.add(a);cities.add(c)
def tour():
    minimum,maximum=999999,0
    def explore(x,path,total):
        nonlocal minimum,maximum
        if len(path)==len(cities):
            minimum,maximum=min(minimum,total),max(maximum,total)
            return
        for y,d in adj[x]:
            if y not in path:explore(y,path+[y],total+d)
    for c in cities:
        explore(c,[c],0)
    return minimum,maximum
part1,part2=tour()
print(part1,part2)