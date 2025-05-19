username = input("enter your username: ")

if username == "rajx":
    print("username found ✅")
else:
    print("username not found ❌ so exiting...")
    exit()

password = input("now enter password: ")
if username == "rajx" and password == "123":
    print("login successful ✅")
else:
    print("login failed ❌")