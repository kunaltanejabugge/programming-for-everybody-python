hours=float(input("enter hours: "))
rate=float(input("enter rate: "))
if hours>40:
    rate=rate*1.5
    pay=rate*hours
    print(pay)
else:
    pay=rate*hours
    print(pay)