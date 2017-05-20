file=open("mbox-short.txt")
count= 0
for line in file:
    line = line.rstrip()
    if line == " ":
        continue
    
    if line.startswith("From"):
        words = line.split()
        if (len(words)) > 2:
            print(words[1])
            count = count + 1
print("there are", count, "line in a file with From as the first word")
            