with open("data/input19.txt") as f:
    L,mol=f.read().strip().split("\n\n")
    L=L.split("\n")
    L=[x.split(" => ") for x in L]

L.sort(key=lambda r:len(r[1]),reverse=True)


def allRep(st,rule):
    a,b=rule
    k=len(a)
    L=[]
    for i in range(len(st)):
        if st[i:i+k]==a:
            L.append(st[:i]+b+st[i+k:])
    return L

def eagerRep(st,allRules):
    L=[]
    for i in range(len(st)):
        if len(L)>1:break #Not sure why it works (doesn't work with 2 or any other number)
        for rule in allRules:
            a,b=rule
            k=len(a)
            if st[i:i+k]==a:
                L.append(st[:i]+b+st[i+k:])
                break
    return L

s=set()
for r in L:
    s.update(allRep(mol,r))
part1=len(s)

invRules=[[b,a] for [a,b] in L]

M=set()
M.add(mol)
newM=set()
part2=0
while "e" not in M:
    part2+=1
    for x in M:
        newM.update(eagerRep(x,invRules))
    M,newM=newM,set()

print(part1,part2)