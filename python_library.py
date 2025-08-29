library = ["Python for Beginners", "Data Structure in C", "AI Basics"]
borrowed_books = []

# Function to display available books
def display_books():
    if not library:
        print("\nNo books available in the library.")
    else:
        print("\nAvailable Books:")
        for book in library:
            print(f"- {book}")

# Function to add a new book
def add_book():
    new_book = input("Enter the name of the book to add: ")
    if new_book not in library:
        library.append(new_book)
        print(f'"{new_book}" has been added to the library.')
    else:
        print("Book already exists in the library.")

# Function to borrow a book
def borrow_book():
    book = input("Enter the name of the book to borrow: ")
    if book in library:
        library.remove(book)
        borrowed_books.append(book)
        print(f'You have borrowed "{book}".')
    else:
        print("Sorry, that book is not available.")

# Function to return a book
def return_book():
    book = input("Enter the name of the book to return: ")
    if book in borrowed_books:
        borrowed_books.remove(book)
        library.append(book)
        print(f'Thank you for returning "{book}".')
    else:
        print("This book was not borrowed from here.")

# Main program loop
while True:
    print("\nLibrary Menu")
    print("1. Display Books")
    print("2. Add Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        display_books()
    elif choice == "2":
        add_book()
    elif choice == "3":
        borrow_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

