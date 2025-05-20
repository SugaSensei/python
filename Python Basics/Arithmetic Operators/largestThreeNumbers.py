a = int(input("Enter first: "))
b = int(input("Enter second: "))
c = int(input("Enter third: "))

#highest
if a >= b and a >= c:
    print("largest number is :", a)
elif b >= a and b >= c:
    print("largest number is :", b)
else:
    print("largest number is :", c)
    

#smallest
if a <= b and a <= c:
    print("smallet number is :", a)
elif b <= a and b <= c:
    print("smallet number is :", b)
else:
    print("smallet number is :", c)

#middle
if (a >=b and a <= c) or (a <= b and a >= c):
    print("middle number is :", a)
elif(b >=a and b <= c) or (b <= a and b >= c):
    print("middle number is :", b)
else:
    print("middle number is :", c)
 