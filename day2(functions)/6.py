def calculate_age(birth_year):
    current_year = 2026
    age = current_year - birth_year
    return age
birth_year = int(input("Enter your birth year: "))

my_age = calculate_age(birth_year)

print("You are", my_age, "years old.")
print(f"Next year, you will be {my_age + 1} years old.")