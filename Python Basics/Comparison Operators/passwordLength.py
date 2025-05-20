password = input("enter the password: ")

if len(password) >= 8:
    print(password,"is strong ✅")
else:
    print(password,"is too short ❌")

print(len(password))