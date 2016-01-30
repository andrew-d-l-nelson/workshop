books = ["Tale of Two Cities", "War and Peace", "Harry Potter", "Lord of the Rings", "The Best of Your Momma Jokes"]
nums = range(0,100)

for book in books:
    print book

nums = range(0,100)
for dumdums in nums: #I use "dumdums" here to emphasize that you can assign any variable to the values in the range of nums
    print dumdums

books = ["Tale of Two Cities", "War and Peace", "Harry Potter", "Lord of the Rings", "The Best of Your Momma Jokes"]

for book in books:
    if book == "Uhoh":
        print book
    else:
        print book

books = ["Tale of Two Cities", "War and Peace", "Harry Potter", "Lord of the Rings", "The Best of Your Momma Jokes"]

for book in books:
    if book == "War and Peace":
        print book

books = ["Tale of Two Cities", "War and Peace", "Harry Potter", "Lord of the Rings", "The Best of Your Momma Jokes"]

for book in books:
    if book == "War and Peace":
        print book
    else:
        print "Not War and Peace"
# For each value in the list, the logical argument is asking, is that value "War and Peace"
# If it isn't, then it spits out "Not War and Peace"
# If the value does match "War and Peace", it spits out War and Peace.
# This is the power of iteration. Things are read iteratively and the outcome is printed out for each value
# Note, it will not print all of the books each time, but only one book at a time.

books = ["Tale of Two Cities", "War and Peace", "Harry Potter", "Lord of the Rings", "The Best of Your Momma Jokes"]

for book in books:
    if book == "War and Peace":
        print (book)
    else:
        print ("Not War and Peace")

nums = range(100)

for n in nums:
    if n % 2 == 0: #In this scenario, the % is taking n, dividing it by 2, and asking if
        # there is anything left over (for example, to the right of the first integer)
        # For example, 5/2 is 2.5. This results in some value left over (0.5), which makes this statement false, so the else is printed
        # However, 4/2 is 2 (there is nothing left over), so this statement is true, and prints out the number
        print(n)
    else:
        pass

# An alternative, longer script below
nums = range(100)

def isEven(n):
    return n % 2 == 0

for n in nums:
    if isEven(n) == True:
        print(n)
    else:
        pass

