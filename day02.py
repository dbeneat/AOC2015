part1,part2=0,0
with open("data/input02.txt") as f:
    for line in f.read().strip().split("\n"):
        a,b,c=sorted([int(x) for x in line.strip().split("x")])
        part1+=3*a*b+2*(b*c+a*c); part2+=2*(a+b)+a*b*c
print(part1,part2)