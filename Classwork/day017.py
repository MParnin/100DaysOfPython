import os
os.system("cls" if os.name == "nt" else "clear")

class User:
    def __init__(self):
        pass

user_1 = User()
user_1.id = "001"
user_1.username = "Bob"

print(user_1.username)