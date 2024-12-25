with open("data/input03.txt") as f:
    inp=f.read().strip()
def F(inp):
    pos=0;visited={pos}
    for x in inp:
        pos+={"<":-1,">":1,"^":-1j,"v":1j}[x]
        visited.add(pos)
    return visited
part1,part2=len(F(inp)),len(F(inp[::2])|F(inp[1::2]))
print(part1,part2)