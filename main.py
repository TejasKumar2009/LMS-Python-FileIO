# Library Management System using Python & FileIO

# Required Functions

# Converting String To List function for convert file content into a list
def convertStrToList(string):
   listOfBooks = list(string.split("\n"))
   return listOfBooks

def fileOps(filename, mode, content=None):
   if(mode=="r"):
      with open(filename, mode) as f:
         text = f.read()
      return text
   else:
      with open(filename, mode) as f:
         f.write(content)

def deleteFileContent(filename, content):
   with open(filename, "r") as f:
      data = f.readlines()

   with open(filename, "w") as f:
       for line in data :
        # condition for data to be deleted
        if line.strip("\n") != content : 
            f.write(line)


# Creating Library Class
class Library:
   # Initializing Library Class
   def __init__(self, listOfBooks, borrowedBooks, borrowedBooksList, borrowedBooksRaw, borrowedBooksListRaw):
      listOfBooks = [book.upper() for book in listOfBooks]
      self.availableBooks = listOfBooks
      self.borrowedBooks = borrowedBooks
      self.borrowedBooksList = borrowedBooksList
      self.borrowedBooksRaw = borrowedBooksRaw
      self.borrowedBooksListRaw = borrowedBooksListRaw

      deleteFileContent("borrowedBooks.txt", "")
      deleteFileContent("borrowedBooks_raw.txt", "")
      deleteFileContent("availableBooks.txt", "")

   # displayAvailableBooks method for Showing Available Books in Library
   def displayAvailableBooks(self):
      print("The List of Available Books in Library are : ")
      for index, book in enumerate(self.availableBooks):
         print(f"\t{index+1}. {book}")

   # displayBorrowedBooks method for Showing All Books in Library
   def displayBorrowedBooks(self):
      print("The List of Available Books in Library are : ")
      for index, borrowedBook in enumerate(self.borrowedBooksList):
         print(f"\t{index+1}. {borrowedBook}")
   
   # requestBook method for Requesting & Borrowing Book from library (if available)
   def requestBook(self, bookName):
      bookName = bookName.upper()

      if(bookName in self.availableBooks):
         self.borrowedBooksList.append(f"{bookName} (borrowed by {username})")

         fileOps("borrowedBooks.txt", "w", "")

         for borrowedBook in self.borrowedBooksList:
            print(borrowedBook)
            fileOps("borrowedBooks.txt", "a", f"\n{borrowedBook}")

         fileOps("borrowedBooks_raw.txt", "a", f"\n{bookName}")

         deleteFileContent("borrowedBooks.txt", "")
         deleteFileContent("borrowedBooks_raw.txt", "")

         self.availableBooks.remove(bookName)

         fileOps("availableBooks.txt", "w", "")
         for book in self.availableBooks:
            fileOps("availableBooks.txt", "a", f"{book}\n")

         deleteFileContent("availableBooks.txt", "")
         print(f"You have been issued {bookName}. Please return it with in 30 days")

      else:
         print(f"Sorry, {bookName} is not Available in Library!!")
 
   
   #donateBook functon simply dontates a book by user
   def donateBook(self, bookName):
      allBooks = fileOps("availableBooks.txt", "a", f"\n{bookName}")
      print(f"Successfully! Your Book '{bookName}' is donated to our Library! Thanks {username} for Donating book on our Platform! :)")


   #returnBook functon returns a book by user that user borrowed
   def returnBook(self, returnBookName, borrowedUser=None):
      # Creating local variables for returnBook method
      isBorrowed = False
      isUsernameMatch = True
      students = fileOps("students.txt", "r")
      students_list = convertStrToList(students)

   # Looping all Usernames
      for index, item in enumerate(students_list):
         returnBookNameCopy = returnBookName.upper()
         returnBookNameCopy = f"{returnBookNameCopy} (borrowed by {item})"

         # basic Checks
         if(returnBookName.upper() in self.borrowedBooksListRaw):

            if(returnBookNameCopy in borrowedBooksList):
               borrowedUser = item
               if(borrowedUser==username):
                  isBorrowed = True
                  deleteFileContent("borrowedBooks.txt", returnBookNameCopy)
                  print(f"{borrowedUser}, Thank You for returning our book!")
               else:
                  isUsernameMatch = False
      
      # isBorrowed or not checks
      if(isBorrowed):
         fileOps("availableBooks.txt", "a", f"\n{returnBookName.upper()}")
         deleteFileContent("borrowedBooks_raw.txt", returnBookName.upper())
         print(f"{returnBookName} is Successfully Returned by {borrowedUser}!!")
      else:
         print("Sorry, This Book Name is Invaild or This Book is not Borrowed!! :|")


#Creating AboutUs Sectione Here
   def aboutUs(self):
      with open("students.txt", "r") as f:
         users_count = f.readlines()

      with open("availableBooks.txt", "r") as f:
         availableBooksCount = f.readlines()

      with open("borrowedBooks.txt", "r") as f:
         borrowedBooksCount = f.readlines()

      self.aboutMsg = f'''\n\t\t==========WELCOME TO OUR ABOUT PAGE==========

      Description : Hello, Everyone I hope you are fine & Welcome to Tejas Library.
                    Tejas Library has more than {len(availableBooksCount)+len(borrowedBooksCount)-1}+ Books & {len(users_count)-1}+ Trusted Users.
                    We rent a book to a user for 30 days max for Free! which is Very Huge for a Book!
                    So, Lets Get Started with us & Create your account now absolutely for Free!! 🔥😊😃
      
      Other Info - 
         App Version 1.0.0
         App Type : CLI
         App Developer : Tejas Kumar\n'''
      print(self.aboutMsg)

# Creating Student Class
class Student:
   # Initializing Student Class
   def __init__(self):
      pass

   # Handling signup confirmation & username using handleSignup method
   def handleSignup(self, confirm_signup=None, signup_username=None):
      confirm_signup = input("If you don't have an account You can create new one by pressing y/n : ")

      if(confirm_signup=="y" or confirm_signup=="Y"):
         signup_username = input("Create a New Username : ")
         student.createStudentAccount(signup_username)

      elif(confirm_signup=="n" or confirm_signup=="N"):
         pass

      else:
         print(f"Invaild Character '{confirm_signup}'! Please Enter y/Y for Create new account & n/N for to do nothing!")
         student.handleSignup()

   # Creating studentLogin method
   def studentLogin(self, studentName=None, action="continue!"):
      global username, student # Using Global variables

      print(f"\nYou must be LoggedIn to {action}")

      # Signup Methods
      student.handleSignup()

      # Handling Login Student name
      studentName = input("Enter your Student Username to Login : ")
      self.studentName = studentName

      # Reading students.txt
      f = fileOps("students.txt", "r")
      students = convertStrToList(f)
      if(studentName in students):
         username = studentName
         print("Congratulations! Your are successfully LoggedIn as", username)
      else:
         print(f"Sorry, Student Username not found!")
         student.studentLogin()

   def createStudentAccount(self, studentName):
      self.studentName = studentName

      # Opening students.txt to get allStudents name
      with open("students.txt", "r") as f:
         allStudents = f.readlines()
      allStudents = [s.replace("\n", "") for s in allStudents]

      # Signup Checks
      if(self.studentName in allStudents):
            print(f"Sorry, Username {self.studentName} is not available, Please Try another!")
      else:
         fileOps("students.txt", "a", f"\n{self.studentName}")
         print(f"Congratulations! Your new Account has been created as {self.studentName}")

   #Creating borrowBook method
   def borrowBook(self):
      self.book = input("Enter the name of the Book You want to Borrow : ")
      return self.book


#Defining Global Variables
username = None

# Reading the availableBooks.txt file and initializing listOfBooks
myBooks = fileOps("availableBooks.txt", "r")
listOfBooks = convertStrToList(myBooks)

# Reading the borrowedBooks.txt file
borrowedBooks = fileOps("borrowedBooks.txt", "r")
borrowedBooksList = convertStrToList(borrowedBooks)

borrowedBooksRaw = fileOps("borrowedBooks_raw.txt", "r")
borrowedBooksListRaw = convertStrToList(borrowedBooksRaw)

# Initializing Library & Student Instance/Object
tejasLibrary = Library(listOfBooks, borrowedBooks, borrowedBooksList, borrowedBooksRaw, borrowedBooksListRaw)

student = Student()
student.studentLogin()

# Looping the Program using while loop
while(True):
   # Showing welcome message
   welcomeMsg = '''\n============ WELCOME TO TEJAS LIBRARY ============
   **Please Choose an option** : 
      1. List All The Available Books
      2. List All The Borrowed Books
      3. Borrow a Book from Library
      4. Return a Book to Library
      5. Donate a Book in Library
      6. About Us
      Q. Quit/Exit TEJAS LIBRARY\n'''
   print(welcomeMsg)

   # Input Choice of user
   input_choice = input("\nEnter Your Choice from Above List are : ")

   # Adding Conditions for different choices
   if(input_choice=="1"):
      tejasLibrary.displayAvailableBooks()

   elif(input_choice=="2"):
      tejasLibrary.displayBorrowedBooks()

   elif(input_choice=="3"):
      bookName = student.borrowBook()
      tejasLibrary.requestBook(bookName)

   elif(input_choice=="4"):
      returnBookName = input("Enter the name of the Book You want to return : ")


      tejasLibrary.returnBook(returnBookName)

   elif(input_choice=="5"):
      donateBookName = input("Enter the Book Name that you want to Donate Us : ")
      tejasLibrary.donateBook(donateBookName)

   elif(input_choice=="6"):
      tejasLibrary.aboutUs()

   elif(input_choice=="Q" or input_choice=="q"):
      print("Thank You for using Tejas Library!! I hope you're enjoying our Library :), Have a Nice Day 😊😊😀")
      exit()
      
   else:
      print(f"Invalid Choice '{input_choice}', Sorry We can't Find your choice! Please Try Again!!")

