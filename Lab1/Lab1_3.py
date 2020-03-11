# Person Class
class Person:
    # Constructor
    def __init__(self, id, fname, lname):
        self.id = id
        self.fname = fname
        self.lname = lname

    # Display first name and last name of person.
    def displayDetails(self):
        print("Name:", self.fname, self.lname)


# Student Class
class Student(Person):
    # Constructor
    def __init__(self, id, fname, lname):
        Person.__init__(self, id, fname, lname)

    # Display first name and last name of student.
    def displayDetails(self):
        print("Student Name:", self.fname, self.lname)


# Faculty Class
class Faculty(Person):
    # Constructor
    def __init__(self, id, fname, lname):
        Person.__init__(self, id, fname, lname)

    # Display first name and last name of faculty.
    def displayDetails(self):
        print("Faculty Name:", self.fname, self.lname)


# Book Class
class Book:
    # Constructor
    def __init__(self, id, name, author=''):
        self.id = id
        self.name = name
        self.author = author


# Library Class
class Library:
    available_books = []
    issued_books = []
    students = []
    facultys = []

    # Constructor
    def __init__(self):
        self

    # Add Book method which will add books to available_books array.
    def addBook(self, book: 'Book'):
        Library.available_books.append(book)

    # Add Student method which will add student to students array.
    def addStudent(self, student: 'Student'):
        Library.students.append(student)

    # Add Faculty method which will add faculty to facultys array.
    def addFaculty(self, faculty: 'Faculty'):
        Library.facultys.append(faculty)

    # Display all AvailableBooks
    def displayAvailableBooks(self):
        for book in self.available_books:
            print(book.name)

    # Display all Students
    def displayStudents(self):
        for student in self.students:
            student.displayDetails()

    # Display all Faculty members
    def displayFacultys(self):
        for faculty in self.facultys:
            faculty.displayDetails()

    # Issue a book to student
    def issueBook(self, book: 'Book'):
        self.issued_books.append(book)
        self.available_books.remove(book)

    # Return book from student
    def returnBook(self, book: 'Book'):
        self.issued_books.remove(book)
        self.available_books.append(book)


# Creating 2 students
s = Student(1, "Murali", "C")
s1 = Student(2, "Murali1", "C1")

# Creating 2 faculty members
f = Faculty(1, "Krishna", "C")
f1 = Faculty(2, "Krishna1", "C1")

# Creating 3 books
b = Book(1, "Java", "sai")
b1 = Book(2, "C#", "C")
b2 = Book(3, "Python", "Ch")

# Creating library class
lib = Library()

# Adding students to library
lib.addStudent(s)
lib.addStudent(s1)

# Adding faculty to library
lib.addFaculty(f)
lib.addFaculty(f1)

# Adding books to library
lib.addBook(b)
lib.addBook(b1)
lib.addBook(b2)

# Displaying operations
print("Displaying all Students : ")
lib.displayStudents()
print("------------------------------------")
print("Displaying all Faculty : ")
lib.displayFacultys()
print("------------------------------------")
print("Displaying all Available Books : ")
lib.displayAvailableBooks()
print("------------------------------------")
lib.issueBook(b)
print("Displaying all Available Books after issuing Java : ")
lib.displayAvailableBooks()
print("------------------------------------")
lib.returnBook(b)
print("Displaying all Available Books after returning Java : ")
lib.displayAvailableBooks()
