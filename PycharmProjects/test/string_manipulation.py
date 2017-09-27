with open("/home/sapling/work/tcpdump.txt", "r") as f:
    searchlines = f.readlines()

for i, line in enumerate(searchlines):
    if "12:44:56" in line:
        for l in searchlines[i:i+3]:
            print ("Number -> " + str(i) + ":" + l,)
            print
