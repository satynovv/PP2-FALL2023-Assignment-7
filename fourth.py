import re
with open('row.txt', 'r') as file:
    text = file.read()
a = re.findall(r"[A-Z][a-z]+", text)
print(a)