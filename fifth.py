import re
text = input()
a = re.findall(r"a.*b$", text)
print(a)