with open("data/input06.txt") as f:
    L=f.read().strip().split("\n")
G1=[[0]*1000 for _ in range(1000)]
G2=[[0]*1000 for _ in range(1000)]
for x in L:
    S=x.split()
    a,b,c=S[-4],S[-3],S[-1]
    x1,y1=[int(x) for x in b.split(",")]
    x2,y2=[int(x) for x in c.split(",")]
    for y in range(y1,y2+1):
        for x in range(x1,x2+1):
            if a=="on":G1[y][x]=1;G2[y][x]+=1
            elif a=="off":G1[y][x]=0;G2[y][x]=max(G2[y][x]-1,0)
            else: G1[y][x]=1-G1[y][x];G2[y][x]+=2
part1,part2=sum(sum(x) for x in G1),sum(sum(x) for x in G2)
print(part1,part2)