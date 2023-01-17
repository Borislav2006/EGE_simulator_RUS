import re

string = "/7867/htht/1g89/htrhr/4523/"
# re.search(pattern, string) — Найти в строке string
# первую строчку, подходящую под шаблон pattern
print(re.search(r'/\d{4}/', string)[0])

from string import ascii_lowercase, ascii_uppercase, digits
