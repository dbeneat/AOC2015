with open("data/input07.txt") as f:
    L=f.read().strip().split("\n")
def func(string):
        if string.isnumeric():return string
        else:return f"f_{string}()"
memo={}    
for line in L:
    line=line.split()
    code=f"def f_{line[-1]}():\n"
    code+=f"    if f_{line[-1]} in memo: return memo[f_{line[-1]}]\n"
    code+="    res="
    if len(line)==3: code+=func(line[0])
    elif line[0]=="NOT": code+=f"65535-f_{line[1]}()"
    elif line[1]=="LSHIFT": code+=f"(f_{line[0]}()<<{line[2]})%65536"
    elif line[1]=="RSHIFT": code+=func(line[0])+f">>{line[2]}"
    elif line[1]=="AND": code+=func(line[0])+f"&f_{line[2]}()"
    elif line[1]=="OR": code+=func(line[0])+f"|f_{line[2]}()"
    else:
        print("ERROR",line)
    code+=f"\n    memo[f_{line[-1]}]=res\n    return res"
    #print(code)
    exec(code)
part1=eval("f_a()")
memo={}
def f_b():
    return part1
part2=eval("f_a()")
print(part1,part2)