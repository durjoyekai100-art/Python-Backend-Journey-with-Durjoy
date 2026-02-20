correct_password = "python123"     # ← this is the secret password

tries_left = 3                     # You start with 3 lives

while tries_left > 0:              # As long as you have tries left...
    password = input("Enter password: ")   # Ask the user to type something

    if password == correct_password:       # Did they type the right one?
        print("Login successful!")         # Yes → great!
        break                              # break = "stop the loop now"

    else:                                  # No, wrong password
        tries_left -= 1                    # Lose 1 try
        print("Wrong password!")

        # Optional: tell them how many tries they have left
        print("You have", tries_left, "tries left.\n")

# ← When we get here, the loop has ended
if tries_left == 0:
    print("Account locked!")