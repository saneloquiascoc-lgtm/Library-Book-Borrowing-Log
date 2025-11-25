library_books = ["book1", "book2", "book3", "book4", "book5","book6","book7","book8","book9","book10"]
borrowed_rec = []

while True:
    print("\n==== Library Book Borrowing System ====")
    print("1. Borrow a book")
    print("2. Return a book")
    print("3. View borrowed books")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nAvailable Books:")
        for i, book in enumerate(library_books, start=1):
            print(f"{i}. {book}")

        if library_books:
            try:
                num = int(input("Enter a book number to borrow (0 to cancel): "))
                if num == 0:
                    print("Cancelled.")
                elif 1 <= num <= len(library_books):
                    name = input("Enter your name: ")
                    borrowed_book = library_books.pop(num - 1)
                    borrowed_rec.append((name, borrowed_book))
                    print(f"\n{name} borrowed '{borrowed_book}'.")
                else:
                    print("Invalid number, sorry!")
            except ValueError:
                print("Please enter a number.")
        else:
            print("No books available.")

    elif choice == "2":
        print("\nBorrowed Records:")
        if not borrowed_rec:
            print("No books to return.")
        else:
            for i, record in enumerate(borrowed_rec, start=1):
                print(f"{i}. {record[1]} - borrowed by {record[0]}")
            try:
                num = int(input("Enter book number to return (0 to cancel): "))
                if num == 0:
                    print("Cancelled.")
                elif 1 <= num <= len(borrowed_rec):
                    name, returned_book = borrowed_rec.pop(num - 1)
                    library_books.append(returned_book)
                    print(f"{name} returned '{returned_book}'.")
                else:
                    print("Invalid number, sorry!")
            except ValueError:
                print("Please enter a number.")

    elif choice == "3":
        print("\n===== Borrowed Records =====")
        if not borrowed_rec:
            print("No books have been borrowed yet.")
        else:
            for i, record in enumerate(borrowed_rec, start=1):
                print(f"{i}. {record[1]} - borrowed by {record[0]}")

    elif choice == "4":
        print("\nThank you for using the Library System!")
        break

    else:
        print("Invalid choice, please try again.")