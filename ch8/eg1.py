file = open("romeo.txt")
arr = list()
for line in file:
    for i in line.split():
        if not i in arr:
            arr.append(i)
arr.sort()
print(arr)