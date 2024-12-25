with open("data/input01.txt") as f:inp=f.read().strip()
x=0
part1=2*inp.count("(")-len(inp)
for i,c in enumerate(inp):
    if c=="(":x+=1
    else:x-=1
    if x<0: part2=i+1;break
print(part1,part2)