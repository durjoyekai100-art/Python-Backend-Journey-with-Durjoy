def login_system():
    correct_password = "python"
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        password = input("Enter password: ")

        if password == correct_password:
            print("Login Successful")
            return
        attempts += 1
        print("Wrong password!")
        print(f"{max_attempts - attempts} attempts remaining. \n")
            
    print("Account locked")
login_system()
           
            