username = input("Enter new username: ")

with open("users.txt", "a") as file:
    file.write(username + "\n")