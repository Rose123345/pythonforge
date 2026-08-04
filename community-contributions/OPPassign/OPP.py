class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        self.grades = []

    def add_grade(self, score):
        self.grades.append(score)

    def calculate_average(self):
        if not self.grades:
            return 0
        average = sum(self.grades) / len(self.grades)
        return int(average) if average.is_integer() else average

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")
        print(f"Average Grade: {self.calculate_average()}")


class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def check_balance(self):
        print(f"Current Balance: {self.balance}")

    def account_details(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")


class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def borrow_book(self):
        if self.available:
            self.available = False
            print("Book borrowed successfully")
        else:
            print("Book is not available")

    def return_book(self):
        self.available = True

    def book_status(self):
        status = "Available" if self.available else "Not Available"
        print(f"Status: {status}")


class Employee:
    def __init__(self, name, position, salary, tax_rate):
        self.name = name
        self.position = position
        self.salary = salary
        self.tax_rate = tax_rate

    def calculate_tax(self):
        return self.salary * self.tax_rate

    def net_salary(self):
        return self.salary - self.calculate_tax()

    def employee_details(self):
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: {self.salary}")
        print(f"Tax Rate: {self.tax_rate}")


class ShoppingCart:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []

    def add_item(self, product, price):
        self.items.append({"product": product, "price": price})

    def remove_item(self, product):
        self.items = [item for item in self.items if item["product"] != product]

    def calculate_total(self):
        return sum(item["price"] for item in self.items)

    def display_cart(self):
        for item in self.items:
            print(f"{item['product']} - {item['price']}")
        print()
        print(f"Total: {self.calculate_total()}")


class Patient:
    def __init__(self, name, age, disease, admitted=False):
        self.name = name
        self.age = age
        self.disease = disease
        self.admitted = admitted

    def admit_patient(self):
        self.admitted = True

    def discharge_patient(self):
        self.admitted = False

    def patient_info(self):
        status = "Admitted" if self.admitted else "Discharged"
        print(f"Patient Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Disease: {self.disease}")
        print(f"Status: {status}")


if __name__ == "__main__":
    student1 = Student("Collins", 22, "Computer Science")
    student1.add_grade(80)
    student1.add_grade(90)
    student1.add_grade(70)
    student1.display_info()

    print()

    account = BankAccount("John Doe", "ACC001", 500)
    account.deposit(300)
    account.withdraw(100)
    account.check_balance()

    print()

    book1 = Book("Python Programming", "Guido van Rossum")
    book1.borrow_book()
    book1.book_status()

    print()

    employee = Employee("Sarah", "Developer", 5000, 0.10)
    print(employee.net_salary())

    print()

    cart = ShoppingCart("Collins")
    cart.add_item("Laptop", 5000)
    cart.add_item("Mouse", 100)
    cart.display_cart()

    print()

    patient1 = Patient("Michael", 30, "Malaria")
    patient1.admit_patient()
    patient1.patient_info()
