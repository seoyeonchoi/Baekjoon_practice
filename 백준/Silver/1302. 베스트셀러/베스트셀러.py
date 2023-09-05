import sys

input = sys.stdin.readline

book_sell = {}
for _ in range(int(input())):
    name = input().rstrip()
    if name in book_sell:
        book_sell[name] += 1
    else:
        book_sell[name] = 0

max_value = max(book_sell.values())
max_books = []

for each in book_sell:
    if book_sell[each] == max_value:
        max_books.append(each)

max_books.sort()
print(max_books[0])

