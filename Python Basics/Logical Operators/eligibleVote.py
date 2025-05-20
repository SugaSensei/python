age = int (input ("enter the age: "))
is_citizen = input("are you a citizen ? (yes/no): ") == "yes"

if age >= 18 and is_citizen:
    print("you can vote")
else:
    print("you cannot vote")
