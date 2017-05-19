largest = None
smallest = None
while True:
    try:
        num = input("Enter a number: ")
        if num == "done":
            break
        print (num)
        num = int(num)
        if largest is None or largest < num:
            largest = num
        elif smallest is None or smallest > num:
             smallest = num
    except ValueError:
        print("Please, enter only numbers.")

print ("Maximum", largest)
print ("Minimum", smallest)