def nice(string):
    pairs=[x+y for x,y in zip(string,string[1:])]
    return sum(x in "aeiou" for x in string)>=3\
            and any(x[0]==x[1] for x in pairs)\
            and all(x not in ["ab","cd","pq","xy"] for x in pairs)

def nice2(string):
    pairs=[x+y for x,y in zip(string,string[1:])]
    triples=[x+y+z for x,y,z in zip(string,string[1:],string[2:])]
    if any(x[0]==x[2] for x in triples):
        pos={}
        for i,x in enumerate(pairs):
            if x not in pos:
                pos[x]=i
            elif i-pos[x]>=2:
                return True
    return False

part1,part2=0,0
with open("data/input05.txt") as f:
    for string in f.read().strip().split("\n"):
        part1+=nice(string)
        part2+=nice2(string)
print(part1,part2)