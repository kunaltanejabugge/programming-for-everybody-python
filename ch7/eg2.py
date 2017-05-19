name = input("enter file name: ")
file = open(name)
count = 0
total = 0
final = 0
for line in file:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    i=line.find(":")
    number=float(line[i+1:])
    total=number+total
final=total/count
print("average spam confidence:",final)