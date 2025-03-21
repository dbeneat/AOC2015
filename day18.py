def sim(isP2):
    with open("data/input18.txt") as f:
        G=f.read().strip().split("\n")
        G=[list(x) for x in G]
        NG=[[x for x in line] for line in G]
        H,W=len(G),len(G[0])
    def get(i,j):
        if isP2 and i in [0,H-1] and j in [0,W-1]: return '#'
        if i<0 or i>=H or j<0 or j>=W: return '.'
        return G[i][j]
    def upd():
        for i in range(H):
            for j in range(W):
                nei=sum(get(ii,jj)=='#' for ii in [i-1,i,i+1] for jj in [j-1,j,j+1] if (ii,jj)!=(i,j))
                if get(i,j)=='.' and nei==3: NG[i][j]='#'
                elif get(i,j)=='#' and nei not in [2,3]: NG[i][j]='.'
                else: NG[i][j]=G[i][j]
    for iter in range(100):
        upd()
        G,NG=NG,G
    return sum(get(i,j)=='#' for i in range(H) for j in range(W))
    
part1,part2=sim(False),sim(True)
print(part1,part2)