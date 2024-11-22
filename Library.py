# project-1
# library management

# a.addbooks
# b.remove books
# c.borrow book
# d.return book
# e.display book


class Library:
    def __init__(self, data):
        self.library = [{'Name': book['Name'], 'Price': book['price'], 'Available': True} for book in data]

    def addbook(self, name, price):
        self.library.append({'Name': name, 'Price': price, 'Available': True})
        print(f"Book '{name}' added successfully.")

    def removebook(self, name):
        for book in self.library:
            if book['Name'] == name:
                self.library.remove(book)
                print(f"Book '{name}' removed successfully.")
                return
        print(f"Book '{name}' not found in the library.")

    def borrowbook(self, name):
        for book in self.library:
            if book['Name'] == name:
                if book['Available']:
                    book['Available'] = False
                    print(f"You have borrowed '{name}'. Please return it after use.")
                    return
                else:
                    print(f"Book '{name}' is currently borrowed by someone else.")
                    return
        print(f"Book '{name}' not found in the library.")

    def returnbook(self, name):
        for book in self.library:
            if book['Name'] == name:
                if not book['Available']:
                    book['Available'] = True
                    print(f"Thank you for returning '{name}'. It is now available for others.")
                    return
                else:
                    print(f"Book '{name}' was not borrowed.")
                    return
        print(f"Book '{name}' not found in the library.")

    def viewbooks(self):
        print("Available Books:")
        for book in self.library:
            availability = "Available" if book['Available'] else "Borrowed"
            print(f"Name: {book['Name']}, Price: {book['Price']}, Status: {availability}")


data = [
    {'Name': 'Atomic Habits', 'price': 600},
    {'Name': 'The Alchemist', 'price': 400},
    {'Name': 'Sapiens: A Brief History of Humankind', 'price': 500},
    {'Name': 'Rich Dad Poor Dad', 'price': 450},
    {'Name': 'Think and Grow Rich', 'price': 350},
    {'Name': 'Ikigai: The Japanese Secret to a Long and Happy Life', 'price': 450},
    {'Name': 'The Power of Your Subconscious Mind', 'price': 250},
    {'Name': 'The Psychology of Money', 'price': 550},
    {'Name': '1984', 'price': 300},
    {'Name': 'The Four Agreement', 'price': 350},
]

p1 = Library(data)

while True:
    print("\nOptions:")
    print("a. Add Book")
    print("b. Remove Book")
    print("c. Borrow Book")
    print("d. Return Book")
    print("e. Display Books")
    print("f. Exit")

    choice = input("Enter your choice (a-f): ")

    if choice == "a":
        name = input("Enter Book Name: ")
        price = float(input("Enter Book Price: "))
        p1.addbook(name, price)
    elif choice == "b":
        name = input("Enter Book Name to Remove: ")
        p1.removebook(name)
    elif choice == "c":
        name = input("Enter Book Name to Borrow: ")
        p1.borrowbook(name)
    elif choice == "d":
        name = input("Enter Book Name to Return: ")
        p1.returnbook(name)
    elif choice == "e":
        p1.viewbooks()
    elif choice == "f":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
