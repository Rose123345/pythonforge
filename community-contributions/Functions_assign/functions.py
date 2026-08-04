#Question 1 – Student Grade Function (15 Marks)

#Write a function named calculate_grade(score) that accepts a student's score and returns the corresponding grade using the table below:
# Function to calculate student's grade

def calculate_grade(score):
    if 80 <= score <= 100:
        return "A"
    elif 70 <= score <= 79:
        return "B"
    elif 60 <= score <= 69:
        return "C"
    elif 50 <= score <= 59:
        return "D"
    else:
        return "F"

# Test the function
scores = [85, 72, 48]

for score in scores:
    print(f"Score: {score}, Grade: {calculate_grade(score)}")

#Question 2 – Shopping Cart Total 
# Function to calculate total cost

def calculate_total(*prices):
    return sum(prices)

# Test
total = calculate_total(25, 40, 15, 20, 30)

print("Total Cost:", total)


# Function to display employee details

def employee_details(**details):
    for key, value in details.items():
        print(f"{key.capitalize()}: {value}")

# Test
employee_details(
    name="John",
    department="IT",
    salary=5000,
    city="Accra"
)

# Function to perform withdrawal

def withdraw(balance, amount):
    if amount > balance:
        return "Insufficient Funds"
    else:
        balance -= amount
        return balance

# Test 1
balance = 1000

print("First Withdrawal:", withdraw(balance, 250))

# Test 2
print("Second Withdrawal:", withdraw(balance, 1500))

# Celsius to Fahrenheit

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Fahrenheit to Celsius

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Test
print("25°C =", celsius_to_fahrenheit(25), "°F")
print("98.6°F =", fahrenheit_to_celsius(98.6), "°C")


# Global list
students = []

# Function to add student
def add_student(name):
    students.append(name)
    print(name, "added successfully.")

# Function to remove student
def remove_student(name):
    if name in students:
        students.remove(name)
        print(name, "removed successfully.")
    else:
        print(name, "not found.")

# Function to display students
def display_students():
    print("\nStudent List:")
    if len(students) == 0:
        print("No students available.")
    else:
        for student in students:
            print(student)

# Function to search student
def search_student(name):
    if name in students:
        print(name, "found in the list.")
    else:
        print(name, "not found.")

# Operations

add_student("Rose")
add_student("John")
add_student("Mary")

display_students()

search_student("John")

remove_student("Mary")

display_students()





