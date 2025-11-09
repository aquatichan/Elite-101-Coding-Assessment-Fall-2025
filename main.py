from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()

class Book:
    def __init__(self, id, title, author, genre, available=True, due_date=None, checkouts=0):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available
        self.due_date = due_date
        self.checkouts = checkouts

    # -------- Level 1 --------
    # TODO: Create a function to view all books that are currently available
    # Output should include book ID, title, and author

    def view_available_books(self, catalog):
        any_available = False
        for book in catalog:
            if book["available"]:
                any_available = True
                print(f"\nID: {book['id']}\nTitle: {book['title']}\nAuthor: {book['author']}\n")
        if not any_available:
            print("\nNo books are available at this time.\n")

    # -------- Level 2 --------
    # TODO: Create a function to search books by author OR genre
    # Search should be case-insensitive
    # Return a list of matching books

    def search_books(self, catalog):
        user_input = input("Enter an author or genre to search for: ").lower()
        results = []
        for book in catalog:
            author_match = user_input in book["author"].lower()
            genre_match = user_input in book["genre"].lower()
            if author_match or genre_match:
                results.append(book)

        if len(results) > 0:
            print("\nMatching books found:\n")
            for book in results:
                print(f"\nID: {book['id']}\nTitle: {book['title']}\nAuthor: {book['author']}\nGenre: {book['genre']}\n")
        else:
            print("\nNo books matched your search query.\n")
        return results

    # -------- Level 3 --------
    # TODO: Create a function to checkout a book by ID
    # If the book is available:
    #   - Mark it unavailable
    #   - Set the due_date to 2 weeks from today
    #   - Increment the checkouts counter
    # If it is not available:
    #   - Print a message saying it's already checked out

    def checkout(self, catalog):
        checkout_id = input("Enter the ID of the book you want to check out: ").upper()
        any_available = False
        for book in catalog:
            if book["id"] == checkout_id:
                any_available = True
                if book["available"]:
                    book["available"] = False
                    book["due_date"] = (datetime.today() + timedelta(weeks=2)).date()
                    book["checkouts"] += 1

                    print(f"\nYou checked out '{book['title']}' by {book['author']}.")
                    print(f"Due date: {book['due_date']}\n")
                    break
                else:
                    print("\nSorry, that book cannot be checked out at this time.\n")
                    break
        if not any_available:
            print("\nNo book was found with the given ID.\n")

    # -------- Level 4 --------
    # TODO: Create a function to return a book by ID
    # Set its availability to True and clear the due_date

    def return_book(self, catalog):
        return_id = input("Enter the ID of the book you want to return: ").upper()
        any_available = False
        for book in catalog:
            if book["id"] == return_id:
                any_available = True
                if not book["available"] and book["due_date"]:
                    book["available"] = True
                    book["due_date"] = None
                    print(f"\nYou returned '{book['title']}' by {book['author']} on {datetime.today().date()}.\n")
                    break
                else:
                    print("\nSorry, that book cannot be returned at this time.\n")
                    break
        if not any_available:
            print("\nNo book was found with the given ID.\n")

    # TODO: Create a function to list all overdue books
    # A book is overdue if its due_date is before today AND it is still checked out

    def list_overdue(self, catalog):
        any_overdue = False
        for book in catalog:
            if not book["available"] and book["due_date"]:
                due_date = datetime.fromisoformat(book["due_date"]).date()
                if due_date < datetime.today().date():
                    any_overdue = True
                    days_overdue = (datetime.today().date() - due_date).days
                    print(
                        f"\nID: {book['id']}\nTitle: {book['title']}\nAuthor: {book['author']}\nDue date: {book['due_date']} ({days_overdue} days overdue)\n")
        if not any_overdue:
            print("\nNo books are overdue at this time.\n")

# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

def main_menu(obj):
    name = input("What is your name?\n")
    while True:
        print(f"{name}'s Library Account - Main Menu"
              "\n1. View available books"
              "\n2. Search by author or genre"
              "\n3. Check out a book"
              "\n4. Return a book"
              "\n5. View overdue books"
              "\n6. Quit")

        choice = int(input("Enter your choice (number from 1-6): "))
        if choice == 1:
            obj.view_available_books(library_books)
        elif choice == 2:
            obj.search_books(library_books)
        elif choice == 3:
            obj.checkout(library_books)
        elif choice == 4:
            obj.return_book(library_books)
        elif choice == 5:
            obj.list_overdue(library_books)
        elif choice == 6:
            print("\nGoodbye!")
            exit()
        else:
            print("\nInvalid input. Please enter a number from 1 to 6.\n")

if __name__ == "__main__":
    # You can use this space to test your functions
    test = Book(**library_books[0])
    main_menu(test)
