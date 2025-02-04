class Bookshop:
    def __init__(self):
        self.books = {}

    def add_book(self, book_title):
        if book_title not in self.books:
            self.books[book_title] = True
            print(f"Книгата {book_title} е добавена.")
        else:
            print(f"Книгата {book_title} е вече налична.")

    def borrow(self, book_title):
        if book_title in self.books:
            if self.books[book_title] == True:
                self.books[book_title] = False
                print(f"Книгата {book_title} е дадена назааем.")
            else:
                print(f"Книгата {book_title} не е налична в момента.")
        else:
            print(f"Книгата {book_title} не е налична в книжарницата.")
    def return_book(self, book_title):
        if book_title in self.books:
            if self.books[book_title] == False:
                self.books[book_title] = True
                print(f"Книгата {book_title} е върната успешно.")
            else:
                print(f"Книгата {book_title} е в наличност вече.")
        else:
            print(f"Книжарницата не е давала книга със заглавие {book_title}, защото не се предлага в нея.")

    def list_available_books(self):
        print("Налични книги за закупуване:")
        for book in self.books:
            if self.books[book] == True:
                print(book)

Bookshop = Bookshop()
Bookshop.add_book("Книга 1")
Bookshop.add_book("Книга 2")
Bookshop.add_book("Книга 3")

Bookshop.borrow("Книга 2")
Bookshop.borrow("Книга 3")

Bookshop.return_book("Книга 3")

Bookshop.list_available_books()
