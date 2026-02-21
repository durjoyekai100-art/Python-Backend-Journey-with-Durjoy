# Mini Project: Simple Username Manager
# Goal: Ask username → save to file → read all usernames → show list
# Bonus: Prevent empty input

FILENAME = "users.txt"  # We'll save usernames here (one per line)

# Step 1: Ask for username (with protection against empty input)
while True:
    username = input("Enter username: ").strip()  # .strip() removes extra spaces
    
    if username == "":  # Check if it's empty after stripping
        print("Username cannot be empty! Please try again.")
        continue
    
    # If we reach here → username is not empty
    break

# Step 2: Save username to file (append mode so we don't overwrite old users)
try:
    with open(FILENAME, "a", encoding="utf-8") as file:
        file.write(username + "\n")  # one username per line
    print(f"Username '{username}' saved successfully!")
except Exception as e:
    print(f"Error saving username: {e}")
    exit()  # stop program if file cannot be written

# Step 3 & 4: Read all users from file and print them nicely
print("\n" + "=" * 40)
print("     ALL REGISTERED USERS")
print("=" * 40)

try:
    with open(FILENAME, "r", encoding="utf-8") as file:
        users = file.readlines()  # read all lines into a list
        
        if not users:
            print("No users registered yet.")
        else:
            for i, user in enumerate(users, start=1):
                clean_user = user.strip()  # remove the \n
                print(f"{i:2d}. {clean_user}")
                
except FileNotFoundError:
    print("No users file found yet. You are the first user!")
except Exception as e:
    print(f"Error reading users: {e}")

print("=" * 40)