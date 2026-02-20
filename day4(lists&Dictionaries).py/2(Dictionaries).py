student = {
    "name" : "Durjoy",   # dictionaries are made of key;value pair
    "roll" : 9 ,
    "cgpa" : 3.9
}

print(student["name"])

student["cgpa"] = 4  # updated 
student["department"] = "Cse" # added
print(student)

for key, value in student.items(): # adding a loop
    print(key, value)
