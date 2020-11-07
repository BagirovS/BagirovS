def print_book_info(title, author=None, year=None):
    #  Write your code here
    if author != None and year != None:
        print('"' + title + '"', 'was written by', author, 'in', year)
    elif author == None and year != None:
        print('"' + title + '"', 'was written in', year)
    elif author != None and year == None:
        print('"' + title + '"', 'was written by', author)
    else:
        print('"' + title + '"',)
    pass


numbers = {"first": 1, "second": 2, "third": 3, "fourth": 4}

#print(numbers.pop())

print(numbers.pop("fourth"))

print(numbers.get(4, "4"))

print(numbers.popitem())

print(numbers.get(4))

print(numbers.get("fourth"))