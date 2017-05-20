file = open("mbox-short.txt")
d = dict()
maxvalue=0
name=""
for line in file:
    line = line.strip()
    if line.startswith("From"):
        words = line.split()
        word = words[1]
        if word not in d:
            d[word] = 1
        else:
            d[word] = d[word] + 1
    else:
        continue
        
bigcount = None
bigword = None
for word, value in d.items():
    if bigcount is None or value > bigcount:
        bigword = word
        bigcount = value

print(bigword, bigcount)