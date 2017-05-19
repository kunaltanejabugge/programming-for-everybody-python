import random

for i in range(10):
    x=random.random()
    print(x)
    
for i in range(10):
    y=random.randint(5,15)
    print(y)
    
a=[1,3,4,5,2,5,6,2,6,8]
print(random.choice(a))