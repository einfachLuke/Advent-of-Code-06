fishlist = open("text06.txt").read().split(",")
infishlist = []
daystocome = 80
dayconter = 1

for fish in fishlist:
    infishlist.append(int(fish))

for fish in infishlist:
    fish += 1

print(infishlist)

print(len(fishlist))
while dayconter <= daystocome:
    print("Day", dayconter)
    for fish in infishlist:
        fish -= 1
        if fish == 0:
            fish = 7
            infishlist.append(9)
    dayconter += 1
    print(len(infishlist))
