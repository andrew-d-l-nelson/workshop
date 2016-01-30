x = 7 # assigning a value to the variable "x"
day = "Saturday"
if x < 10:   #This is a boolian expression here.
    print("The day is " + day +
    ". What a great day!")
else:
    print("I don't think that will happen")

x = 7
day = "Saturday"
if x < 10:   #This is a boolian expression here.
    print("The day is " + str(x) + " " + day + #we can include extra spaces by surrounding them with quotes.
    #Also, to add an integer in the middle of a string, you have to convert it to a str
    ". What a great day!")
else:
    print("I don't think that will happen")

# To make more sense of this statement:
x = 7
date = "30th"
day = "Saturday"
if x < 10:
    print("The day is " + day + " the " + date +
    ". What a lousy day!")
else:
    print("I don't think that will happen")

books = ["Harry Potter", "The Tale of Two Cities"]
if books:
    print books

books = ["Harry Potter", "The Tale of Two Cities"]
if books:
    print books[1] #This is asking the statement to print out the second item in the list
    # The result will be 'The Tale of Two Cities'

x = 7
date = "30th"
day = "Saturday"
if x < 10:
    print("The day is " + day + " the " + date +
    ". What a lousy day!")
elif day == "Saturday": #This second if statement will only be used if the first "if"
    # comes back as negative, but only if it is written as elif.
    # If it is written as "if" then it will only print out if the day is saturday and x > 10
    print "I hate Saturday"
else:
    print("I don't think that will happen")

x = 70
date = "30th"
day = "Saturday"
if x < 10:
    print("The day is " + day + " the " + date +
    ". What a lousy day!")
elif day == "Friday": #The final "else" will only print out if the
    # first two statements are false, as is the case here.
    print "I hate Saturday"
else:
    print("I don't think that will happen")