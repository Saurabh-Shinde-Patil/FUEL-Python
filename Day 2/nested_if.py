

username=input("enter user name:")
password=int(input("enter password:"))

if username =="admin":
    if password ==1234:
        print("login success")
    else:
        print("wrong password")
else:
    print("unn=known user")            