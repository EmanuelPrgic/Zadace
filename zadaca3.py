import re

txt = input("Unesite string: ")
regex = "\Ae\s\b[0-5]p\Z"

result = re.findall(regex, txt)

print(result)
if result:
    print(result)
else:
    print("Ne")
