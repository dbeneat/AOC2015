with open("data/input16.txt") as f:
    L=f.read().strip().split("\n")

constraints1=[
"children: 3",
"cats: 7",
"samoyeds: 2",
"pomeranians: 3",
"akitas: 0",
"vizslas: 0",
"goldfish: 5",
"trees: 3",
"cars: 2",
"perfumes: 1"
]

constraints2=[
"children: 3",
"cats: 8","cats: 9","cats: 10",
"samoyeds: 2",
"pomeranians: 2","pomeranians: 1","pomeranians: 0",
"akitas: 0",
"vizslas: 0",
"goldfish: 4","goldfish: 3","goldfish: 2","goldfish: 1","goldfish: 0",
"trees: 4","trees: 5","trees: 6","trees: 7","trees: 8","trees: 9","trees: 10",
"cars: 2",
"perfumes: 1"
]

for line in L:
    if all(x.strip() in constraints1 for x in line.split(":",1)[1].split(",")):
        print("part 1:",line)
    if all(x.strip() in constraints2 for x in line.split(":",1)[1].split(",")):
        print("part 2:",line)