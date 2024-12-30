import json
with open("data/input12.txt") as f:j=json.load(f)
def addition(M,ispart2):   
    if type(M)==list:return sum(addition(x,ispart2) for x in M)
    if type(M)==dict:
        if ispart2 and "red" in M.values(): return 0
        return sum(addition(x,ispart2)+addition(M[x],ispart2) for x in M)
    if type(M)==str:return 0
    if type(M)==int:return M
    print("unknown type:",M,type(M))
print(addition(j,False),addition(j,True))