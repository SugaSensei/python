a = int(input("Enter first: "))
b = int(input("Enter second: "))
c = int(input("Enter third: "))

if a >= b and a >= c:
    print("largest number is :", a)
elif b >= a and b >= c:
    print("largest number is :", b)
else:
    print("largest number is :", c)
    
    