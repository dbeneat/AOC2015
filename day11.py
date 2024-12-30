with open("data/input11.txt") as f:
    pwd=list(f.read().strip())
alph="abcdefghijklmnopqrstuvwxyz"
trAlph=[x+y+z for x,y,z in zip(alph,alph[1:],alph[2:])]
def inc(L,n):
    for i,x in enumerate(L):
        if x in "iol":
            L[i]=chr(ord(L[i])+1)
            for j in range(i+1,len(L)):
                L[j]="a"
            return
    if L[n]=="z":L[n]="a";inc(L,n-1);return
    L[n]=chr(ord(L[n])+1)
    if L[n] in "iol":L[n]=chr(ord(L[n])+1)

def ok(L):
    pairs=[x+y for x,y in zip(L,L[1:])]
    triples=[x+y+z for x,y,z in zip(L,L[1:],L[2:])]
    if any(t in trAlph for t in triples):
        last=None   
        for i,p in enumerate(pairs):
            if p[0]==p[1]:
                if last==None:last=i
                elif i-last>=2:return True
    return False

while not ok(pwd):inc(pwd,-1)
part1="".join(pwd)
inc(pwd,-1)
while not ok(pwd):inc(pwd,-1)
part2="".join(pwd)
print(part1,part2)