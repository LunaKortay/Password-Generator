import json
from secrets import choice

char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!'^^+%&/()=?_-.,"

length = int(input("Please Enter The Lenght You Want For Your Password To Be: "))
whereToUse = str(input("Where Are You Going To Use This Password?: "))
passwords= []
with open("store_password.json", "r") as f:
    storedpasswords = json.load(f)


password = ''.join(choice(char) for _ in range(length))
   
passwords = {"WhereToUse": whereToUse, "Password": password}
storedpasswords["passwords"].append(passwords)


with open("store_password.json", "w") as f:
    json.dump(storedpasswords, f, indent=2)

