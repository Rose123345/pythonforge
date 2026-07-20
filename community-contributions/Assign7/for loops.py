# que 1 Student Information Manager

# Create a program that asks the user to enter the names and marks of five students. Store the data in a dictionary where the student's name is the key and the mark is the value.

students = {}

for i in range(5):
    name = input(f"Enter student {i+1} name: ")
    mark = float(input("Enter mark: "))
    students[name] = mark

print("\nStudent Records")
for name, mark in students.items():
    print(f"{name}: {mark}")

marks = list(students.values())

print("Highest Mark:", max(marks))
print("Lowest Mark:", min(marks))
print("Average Mark:", sum(marks) / len(marks))

print("\nStudents who scored 50 or above:")
for name, mark in students.items():
    if mark >= 50:
        print(name)

# Question 2: Word Analyzer
sentence = input("Enter a sentence: ")

words = sentence.split()

vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for char in sentence:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Total characters:", len(sentence))
print("Total words:", len(words))
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Reversed:", sentence[::-1])
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)

print("\nWord Frequency")
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

for word, count in frequency.items():
    print(word, ":", count)


# Question 3: Sales Report  

products = {
    "Laptop": 5000,
    "Phone": 3000,
    "Tablet": 2500,
    "Printer": 1500,
    "Mouse": 100
}

sales = {}

for product, price in products.items():
    qty = int(input(f"Enter quantity sold for {product}: "))
    sales[product] = price * qty

print("\nSales Report")
for product in products:
    qty_sales = sales[product] / products[product]
    print(product,
          "Price:", products[product],
          "Qty:", int(qty_sales),
          "Sales:", sales[product])

print("Grand Total:", sum(sales.values()))

highest = max(sales, key=sales.get)
lowest = min(sales, key=sales.get)

print("Highest Sales Product:", highest)
print("Lowest Sales Product:", lowest)

# Question 4: Employee Salary Processor
employees = []

for i in range(5):
    name = input("Enter employee name: ")
    salary = float(input("Enter basic salary: "))

    tax = salary * 0.10
    bonus = salary * 0.05
    net_salary = salary + bonus - tax

    employees.append([name, salary, tax, bonus, net_salary])

print("\nSalary Report")
print("-" * 60)

for emp in employees:
    print(f"Name: {emp[0]}")
    print(f"Basic Salary: {emp[1]:.2f}")
    print(f"Tax: {emp[2]:.2f}")
    print(f"Bonus: {emp[3]:.2f}")
    print(f"Net Salary: {emp[4]:.2f}")
    print("-" * 60)


# Question 5: Inventory Management System
inventory = {}

while True:
    print("\n1. Add Item")
    print("2. Update Quantity")
    print("3. Remove Item")
    print("4. Display Items")
    print("5. Search Item")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        item = input("Item name: ")
        qty = int(input("Quantity: "))
        inventory[item] = qty

    elif choice == "2":
        item = input("Item to update: ")
        if item in inventory:
            qty = int(input("New quantity: "))
            inventory[item] = qty
        else:
            print("Item not found.")

    elif choice == "3":
        item = input("Item to remove: ")
        inventory.pop(item, None)

    elif choice == "4":
        for item, qty in inventory.items():
            print(item, ":", qty)

    elif choice == "5":
        item = input("Search item: ")
        if item in inventory:
            print(item, "Quantity:", inventory[item])
        else:
            print("Item not found.")

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")


# Question 6: Student Grade Report
students = {}

for i in range(10):
    name = input("Enter student name: ")
    mark = float(input("Enter mark: "))
    students[name] = mark

grades_count = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

print("\nGrade Report")

for name, mark in students.items():

    if mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    elif mark >= 50:
        grade = "D"
    else:
        grade = "F"

    grades_count[grade] += 1

    print(f"{name} - {mark} - {grade}")

marks = list(students.values())

print("\nGrade Summary")
for grade, count in grades_count.items():
    print(grade, ":", count)

print("Highest Mark:", max(marks))
print("Lowest Mark:", min(marks))
print("Average Mark:", sum(marks) / len(marks))


# Question 7: Dictionary and Set Challenge
countries = {
    "Ghana": "Accra",
    "Nigeria": "Abuja",
    "Kenya": "Nairobi",
    "Egypt": "Cairo",
    "France": "Paris",
    "Germany": "Berlin",
    "Brazil": "Brasilia",
    "China": "Beijing"
}

continents = {
    "Africa",
    "Europe",
    "South America",
    "Asia"
}

print("Countries:")
for country in countries.keys():
    print(country)

print("\nCapitals:")
for capital in countries.values():
    print(capital)

print("\nCountry and Capital")
for country, capital in countries.items():
    print(country, "->", capital)

print("\nUnique Continents:")
for continent in continents:
    print(continent)

print("Number of Continents:", len(continents))

search = input("\nEnter country to search: ")

if search in countries:
    print("Capital:", countries[search])
else:
    print("Country not found.")

# Question 8: Mini Banking System
balance = 2000
transactions = []

total_deposit = 0
total_withdrawal = 0

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. View Transaction History")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Balance: GHS", balance)

    elif choice == "2":
        amount = float(input("Enter amount: "))
        balance += amount
        total_deposit += amount
        transactions.append(f"Deposited GHS {amount}")

    elif choice == "3":
        amount = float(input("Enter amount: "))

        if amount <= balance:
            balance -= amount
            total_withdrawal += amount
            transactions.append(f"Withdrawn GHS {amount}")
        else:
            print("Insufficient funds!")

    elif choice == "4":
        print("\nTransaction History")
        for t in transactions:
            print(t)

    elif choice == "5":
        break

    else:
        print("Invalid choice")

print("\nFinal Report")
print("Final Balance: GHS", balance)
print("Total Deposited: GHS", total_deposit)
print("Total Withdrawn: GHS", total_withdrawal)
print("Number of Transactions:", len(transactions))



