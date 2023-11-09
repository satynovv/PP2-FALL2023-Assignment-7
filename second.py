import re
with open('row.txt', 'r') as file:
    text = file.read()
a = re.findall(r"ab{2,3}", text)
print(a)
