class Book:
    # Represents a book in a small personal library.
    # Demonstrates OOP with attributes, methods, and basic state management.

    def __init__(self, title, author, year, status="available"):
        self.title = title.strip()
        self.author = author.strip()
        self.year = year
        self.status = status.lower() # "available" or "borrowed"
        
        if not self.title:
            raise ValueError("Title cannot be empty")
        if not self.author:
            raise ValueError("Author cannot be empty")
        if not isinstance(year, int) or year < 0 or year > 2100:
            raise ValueError("Year must be a reasonable integer (0–2100)")

    def borrow(self):
        # Mark the book as borrowed if it is currently available.
        if self.status == "available":
            self.status = "borrowed"
            print(f"→ You have borrowed '{self.title}' by {self.author}.")
        else:
            print(f"× '{self.title}' is already borrowed.")

    def return_book(self):
        # Mark the book as available again if it was borrowed.
        if self.status == "borrowed":
            self.status = "available"
            print(f"→ You have returned '{self.title}'.")
        else:
            print(f"× '{self.title}' was not borrowed.")

    def display_info(self):
        # Return a formatted string with book details.
        return (f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"Year: {self.year}\n"
                f"Status: {self.status.capitalize()}")


def main():
    print("=== Personal Library Manager (Lab Activity 2) ===\n")
    books = []

    while True:
        print("\nOptions:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Show all books")
        print("5. Quit")

        try:
            choice = input("\nEnter actions: ").strip()

            if choice == "1":
                title = input("Book title: ").strip()
                author = input("Author name: ").strip()
                
                while True:
                    try:
                        year = int(input("Publication year: ").strip())
                        break
                    except ValueError:
                        print("! Please enter a valid year (number).")

                book = Book(title, author, year)
                books.append(book)
                print(f"✓ Book '{title}' added successfully.")

            elif choice == "2":
                if not books:
                    print("! No books in library yet.")
                    continue
                    
                title = input("Enter title to borrow: ").strip().lower()
                found = False
                for book in books:
                    if book.title.lower() == title:
                        book.borrow()
                        found = True
                        break
                if not found:
                    print(f"! No book found with title '{title}'.")

            elif choice == "3":
                if not books:
                    print("! No books in library yet.")
                    continue
                    
                title = input("Enter title to return: ").strip().lower()
                found = False
                for book in books:
                    if book.title.lower() == title:
                        book.return_book()
                        found = True
                        break
                if not found:
                    print(f"! No book found with title '{title}'.")

            elif choice == "4":
                if not books:
                    print("No books in the library yet.")
                else:
                    print("\n--- Library Collection ---")
                    for i, book in enumerate(books, 1):
                        print(f"\nBook #{i}")
                        print(book.display_info())
                        print("-" * 40)

            elif choice == "5":
                print("\nThank you for using the Library Manager. Goodbye!")
                break

            else:
                print("! Invalid choice. Please enter 1–5.")

        except ValueError as e:
            print(f"Input error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
            print("Please try again.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user. Goodbye!")
    except Exception as e:
        print(f"Critical error: {e}")
        print("Program will exit.")