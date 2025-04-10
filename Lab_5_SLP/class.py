class home_library():
    def __init__(self, title, author, genre, year, pages):
        
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
        self.pages = pages
        
book1 = home_library("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 1925, 180)
book2 = home_library("To Kill a Mockingbird", "Harper Lee", "Fiction", 1960, 281)
book3 = home_library("1984", "George Orwell", "Dystopian", 1949, 328)
book4 = home_library("Pride and Prejudice", "Jane Austen", "Romance", 1813, 279)
book5 = home_library("The Catcher in the Rye", "J.D. Salinger", "Fiction", 1951, 277)
book6 = home_library("The Hobbit", "J.R.R. Tolkien", "Fantasy", 1937, 310)

print(book1.title)