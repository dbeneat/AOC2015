with open("data/input20.txt") as f:
    N=int(f.read())

L,M=[0]*1000000,[0]*1000000
for i in range(1,len(L)):
    for k in range(i,len(L),i):
        L[k]+=10*i
        if k<=50*i:
            M[k]+=11*i
    
for i,x in enumerate(L):
    if x>N:
        part1=i
        break

for i,x in enumerate(M):
    if x>N:
        part2=i
        break
        
print(part1,part2)