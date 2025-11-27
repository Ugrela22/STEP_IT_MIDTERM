class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
    
    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'publication_year': self.publication_year
        }
    
    @staticmethod
    def from_dict(data):
        return Book(
            title=data['title'],
            author=data['author'],
            publication_year=data['publication_year']
        )
    
    def __str__(self):
        return f"სათაური: {self.title}, ავტორი: {self.author}, გამოცემის წელი: {self.publication_year}"



# book_manager.py

import json
import os

class BookManager:
    def __init__(self, filename='books_data.json'):
        self.books = []
        self.filename = filename
        self.load_from_file()
    
    def save_to_file(self):
        try:
            books_data = [book.to_dict() for book in self.books]
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump(books_data, file, ensure_ascii=False, indent=4)
            print(f"💾 მონაცემები შენახულია ფაილში: {self.filename}")
        except Exception as e:
            print(f"❌ შეცდომა ფაილში ჩაწერისას: {e}")
    
    def load_from_file(self):
        if not os.path.exists(self.filename):
            print(f"📂 ფაილი {self.filename} არ არსებობს. იქმნება ახალი ბაზა...")
            self.create_initial_data()
            return
        
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                books_data = json.load(file)
            
            self.books = [Book.from_dict(data) for data in books_data]
            print(f"✓ ჩაიტვირთა {len(self.books)} წიგნი ფაილიდან {self.filename}")
        
        except json.JSONDecodeError:
            print(f"❌ შეცდომა: {self.filename} ფაილი დაზიანებულია!")
            print("📂 იქმნება ახალი ბაზა...")
            self.books = []
            self.create_initial_data()
            
        except Exception as e:
            print(f"❌ შეცდომა ფაილის წაკითხვისას: {e}")
            self.books = []
    
    def create_initial_data(self):
        initial_books = [
            Book("ვეფხისტყაოსანი", "შოთა რუსთაველი", 1200),
            Book("ალუდა ქეთელაური", "ვაჟა-ფშაველა", 1888),
            Book("მთვარის მოტაცება", "კონსტანტინე გამსახურდია", 1934)
        ]
        
        for book in initial_books:
            self.books.append(book)
        
        self.save_to_file()
        print(f"✓ შეიქმნა საწყისი მონაცემები: {len(initial_books)} წიგნი")
    
    def add_book(self, book):
        self.books.append(book)
        self.save_to_file()
        print(f"✓ წიგნი '{book.title}' წარმატებით დაემატა!")
    
    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                self.save_to_file()
                print(f"✓ წიგნი '{title}' წარმატებით წაიშალა!")
                return True
        print(f"✗ წიგნი სათაურით '{title}' ვერ მოიძებნა!")
        return False
    
    def search_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]
    
    def search_by_author(self, author):
        return [book for book in self.books if author.lower() in book.author.lower()]
    
    def search_by_year(self, year):
        return [book for book in self.books if book.publication_year == year]
    
    def display_all_books(self):
        if not self.books:
            print("\n📚 ბიბლიოთეკა ცარიელია!")
            return
        
        print(f"\n📚 ბიბლიოთეკაში არის {len(self.books)} წიგნი:")
        print("-" * 80)
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book}")
        print("-" * 80)


# validation.py

def validate_title(title):
    if not title or title.strip() == "":
        return False, "სათაური არ შეიძლება იყოს ცარიელი!"
    if len(title.strip()) < 2:
        return False, "სათაური უნდა შეიცავდეს მინიმუმ 2 სიმბოლოს!"
    return True, ""


def validate_author(author):
    if not author or author.strip() == "":
        return False, "ავტორი არ შეიძლება იყოს ცარიელი!"
    if len(author.strip()) < 2:
        return False, "ავტორი უნდა შეიცავდეს მინიმუმ 2 სიმბოლოს!"
    return True, ""


def validate_year(year_str):
    try:
        year = int(year_str)
        if year < 1000:
            return False, "გამოცემის წელი უნდა იყოს მინიმუმ 1000!"
        if year > 2025:
            return False, "გამოცემის წელი არ შეიძლება იყოს მომავალში!"
        return True, year
    except ValueError:
        return False, "გამოცემის წელი უნდა იყოს რიცხვი!"


def print_menu():
    print("\n" + "=" * 80)
    print("📚 წიგნების მართვის სისტემა".center(80))
    print("=" * 80)
    print("\n1. ახალი წიგნის დამატება")
    print("2. წიგნის წაშლა")
    print("3. წიგნის ძიება სათაურით")
    print("4. წიგნის ძიება ავტორით")
    print("5. წიგნის ძიება გამოცემის წლით")
    print("6. ყველა წიგნის ნახვა")
    print("0. გასვლა")
    print("-" * 80)


def add_book_interface(manager):
    print("\n➕ ახალი წიგნის დამატება")
    print("-" * 40)
    
    while True:
        title = input("შეიყვანეთ წიგნის სათაური: ").strip()
        is_valid, error_msg = validate_title(title)
        if is_valid:
            break
        else:
            print(f"❌ {error_msg}")
    
    while True:
        author = input("შეიყვანეთ ავტორი: ").strip()
        is_valid, error_msg = validate_author(author)
        if is_valid:
            break
        else:
            print(f"❌ {error_msg}")
    
    while True:
        year_input = input("შეიყვანეთ გამოცემის წელი: ").strip()
        is_valid, result = validate_year(year_input)
        if is_valid:
            year = result
            break
        else:
            print(f"❌ {result}")
    
    book = Book(title, author, year)
    manager.add_book(book)


def remove_book_interface(manager):
    print("\n➖ წიგნის წაშლა")
    print("-" * 40)
    
    if not manager.books:
        print("📚 ბიბლიოთეკა ცარიელია!")
        return
    
    title = input("შეიყვანეთ წასაშლელი წიგნის სათაური: ").strip()
    manager.remove_book(title)


def search_by_title_interface(manager):
    print("\n🔍 ძიება სათაურით")
    print("-" * 40)
    
    title = input("შეიყვანეთ სათაური: ").strip()
    results = manager.search_by_title(title)
    
    display_search_results(results, f"სათაური '{title}'")


def search_by_author_interface(manager):
    print("\n🔍 ძიება ავტორით")
    print("-" * 40)
    
    author = input("შეიყვანეთ ავტორი: ").strip()
    results = manager.search_by_author(author)
    
    display_search_results(results, f"ავტორი '{author}'")


def search_by_year_interface(manager):
    print("\n🔍 ძიება გამოცემის წლით")
    print("-" * 40)
    
    while True:
        year_input = input("შეიყვანეთ გამოცემის წელი: ").strip()
        is_valid, result = validate_year(year_input)
        if is_valid:
            year = result
            break
        else:
            print(f"❌ {result}")
    
    results = manager.search_by_year(year)
    display_search_results(results, f"წელი {year}")


def display_search_results(results, search_criteria):
    if not results:
        print(f"\n❌ წიგნი არ მოიძებნა კრიტერიუმით: {search_criteria}")
        return
    
    print(f"\n✓ მოიძებნა {len(results)} წიგნი:")
    print("-" * 80)
    for i, book in enumerate(results, 1):
        print(f"{i}. {book}")
    print("-" * 80)

def main():
    print("=" * 80)
    print("📚 წიგნების მართვის სისტემა ჩაიტვირთა".center(80))
    print("=" * 80)
    
    manager = BookManager()
    
    while True:
        print_menu()
        
        choice = input("\nაირჩიეთ ოპერაცია (0-6): ").strip()
        
        if choice == "1":
            add_book_interface(manager)
        elif choice == "2":
            remove_book_interface(manager)
        elif choice == "3":
            search_by_title_interface(manager)
        elif choice == "4":
            search_by_author_interface(manager)
        elif choice == "5":
            search_by_year_interface(manager)
        elif choice == "6":
            manager.display_all_books()
        elif choice == "0":
            print("\n" + "=" * 80)
            print("👋 მადლობა პროგრამის გამოყენებისთვის!".center(80))
            print(f"💾 ყველა მონაცემი შენახულია ფაილში: {manager.filename}".center(80))
            print("=" * 80)
            break
        else:
            print("\n❌ არასწორი არჩევანი! გთხოვთ აირჩიოთ 0-დან 6-მდე.")
        
        input("\nდააჭირეთ Enter-ს გასაგრძელებლად...")


if __name__ == "__main__":
    main()
