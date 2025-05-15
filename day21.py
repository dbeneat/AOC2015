with open("data/input21.txt") as f:
    L=f.read().strip().split("\n")
    L=[int(x.split(":")[1]) for x in L]
    bossHP,bossDAM,bossAR=L[0],L[1],L[2]

def sim(hp,dmg,ar,hp2,dmg2,ar2,debug=False):
    who,who2="player","boss"
    while True:
        hp2-=max(1,dmg-ar2)
        if debug:
            print(who,"hits",who2, hp2)
        if hp2<=0:
            return who
        who,hp,dmg,ar,who2,hp2,dmg2,ar2=who2,hp2,dmg2,ar2,who,hp,dmg,ar

weapons=[(8,4,0),(10,5,0),(25,6,0),(40,7,0),(74,8,0)]    
armor=[(0,0,0),(13,0,1),(31,0,2),(53,0,3),(75,0,4),(102,0,5)]
rings=[(0,0,0),(0,0,0),(25,1,0),(50,2,0),(100,3,0),(20,0,1),(40,0,2),(80,0,3)]
allItems=weapons+armor[1:]+rings[2:]

worstcost=0
bestcost=1000000
for w in weapons:
    for a in armor:
        for ir1 in range(len(rings)-1):
            r1=rings[ir1]
            for ir2 in range(ir1+1,len(rings)):
                r2=rings[ir2]
                cost=w[0]+a[0]+r1[0]+r2[0]
                dam=w[1]+a[1]+r1[1]+r2[1]
                arm=w[2]+a[2]+r1[2]+r2[2]
                if sim(100,dam,arm,bossHP,bossDAM,bossAR)=="player" and cost<bestcost:
                    bestcost=cost
                if sim(100,dam,arm,bossHP,bossDAM,bossAR)=="boss" and cost>worstcost:
                    worstcost=cost

print(bestcost,worstcost)