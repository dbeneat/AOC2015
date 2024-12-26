with open("data/input08.txt") as f:
    L=f.read().strip().split("\n")
def f(string):
    return 2+len(string)+string.count('"')+string.count("\\")
part1=sum(len(inp)-len(eval(inp)) for inp in L)
part2=sum(f(inp)-len(inp) for inp in L)
print(part1,part2)