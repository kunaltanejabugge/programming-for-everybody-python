file = open("mbox-short.txt")
d = dict()
for line in file:
    if line.startswith("From") and len(line.split()) > 2:
        words = line.split()
        if not words[5][:2] in d:
            d[words[5][:2]] = 1
        else:
            d[words[5][:2]] += 1
        
key = sorted(d)
for i in key:
    print("%s %d" % (1,d[i]))