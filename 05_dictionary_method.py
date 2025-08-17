# Creating a dictionary
student = {
    "name": "Gopal",
    "age": 21,
    "course": "BTech"
}


print("Name==",student["name"])

# 1. get()
print("Name:", student.get("name"))            # Gopal
print("Email:", student.get("email", "N/A"))   # N/A (default)

# 2. keys(), values(), items()
print("\nKeys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# 3. update()
student.update({"email": "gopal@example.com", "age": 22})
student.update(city="Gurgaon")  # another way
print("\nUpdated Student:", student)

# 4. pop()
student.pop("course")  # removes 'course'
print("\nAfter pop('course'):", student)

# 5. popitem()
student.popitem()  # removes last inserted (city)
print("After popitem():", student)

# 6. setdefault()
student.setdefault("course", "BTech")  # re-add course if not present
student.setdefault("name", "Someone")  # 'name' already exists, no change
print("\nAfter setdefault():", student)

# 7. copy()
student_copy = student.copy()
print("\nCopy of student:", student_copy)

# 8. fromkeys()
keys = ["math", "science", "english"]
marks = dict.fromkeys(keys, 0)  # all subjects start with 0 marks
print("\nMarks Dictionary:", marks)

# 9. clear()
marks.clear()
print("After clear():", marks)

# 10. Looping with items()
print("\nLooping over student dictionary:")
for key, value in student.items():
    print(f"{key} => {value}")



del student["age"]
student["email"] = "alice@example.com"

print(student)