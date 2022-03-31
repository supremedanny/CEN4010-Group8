# Book rating and commenting API

import datetime

rating = 0
ISBN = ""
arating = 0.0
username = ""
bookname = ""
comment = ""
purchased = 0  # 0 is false, 1 is true

# Rating: (Add a rating from 1 to 5)
rating = input("Enter a rating from 1 to 5: ")
while (int(rating) < 1 or int(rating) > 5):
    rating = input("Please enter a rating from 1 to 5: ")
ratingtime = datetime.datetime.now()

comment = input("Enter comment: ")
commenttime = datetime.datetime.now()

print(ratingtime, commenttime)

