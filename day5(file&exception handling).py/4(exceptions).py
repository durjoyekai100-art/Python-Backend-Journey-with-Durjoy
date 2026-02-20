try:
    age = int(input("Enter age: "))
    print(100 / age)

except ValueError:
    print("Please enter a number")

except ZeroDivisionError:
    print("Age cannot be zero")