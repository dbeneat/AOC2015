from hashlib import md5
with open("data/input04.txt") as f:
    key=f.read().strip()
n=0
while md5(f"{key}{n}".encode()).hexdigest()[:5]!="00000":n+=1
part1=n
while md5(f"{key}{n}".encode()).hexdigest()[:6]!="000000":n+=1
part2=n
print(part1,part2)