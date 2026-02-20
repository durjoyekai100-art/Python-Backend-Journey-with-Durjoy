username = input("Enter your name: ").strip()

if not username:
    print("username can't be empty!")

else:

  with open("user.txt", "a") as file:
    file.write(username + "\n")
  print("User saved succesfully!")
    
  with open("user.txt", "r") as file:
    data = file.read()
    
