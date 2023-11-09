import re 
text=input()
a = re.findall(r"[a-z][_][a-z]", text)
print(a)