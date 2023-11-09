import re
with open('row.txt', 'r') as file:
    text = file.read()
a=re.sub("[ ,.]","|",text)
print(a)