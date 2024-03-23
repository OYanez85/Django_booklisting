# from typing import DefaultDict

print("Hello world!")

def getTax(base, rate):
    return base * rate
    
x = 0
while x < 5:
    x += 1
    print(x)

print("The value of PI is", 22/7)

pairs = {
    "sally" : 5,
    "harry" : 10
}

print ("Tax is:", getTax(25.13, 0.08))
print(pairs)

key = "sally"
print(pairs.get(key))

set2 = pairs.copy()

print(set2.get(key))