import re
patt = r'4*'
with open('row.txt', 'r') as file:
     text = file.read()
a=re.findall(patt, text)
print(a)