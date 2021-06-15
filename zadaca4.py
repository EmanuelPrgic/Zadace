import re

#ime = input("Unesite ime: ")
#prezime = input("Unesite prezime: ")

#ime = ime.lower()
#prezime = prezime.lower()

mail = input("Unesite email: ")
mail = mail.lower()

regex = "^(.*[a-z])\.(.*[a-z])(@fpmoz.sum.ba)$"
#regex = re.escape(ime) + "." + re.escape(prezime) + "@fpmoz.sum.ba"

result = re.match(regex, mail)

if result:
    print("Uspjesno")
else:
    print("Neuspjesno")

print(30*"-")

eduid = input("Unesite eduId: ")
eduid = eduid.lower()

regex = "^([a-z])(.*[a-z])(\d?)(@sum.ba)$"
#regex = re.escape(ime[0]) + re.escape(prezime) + "(\d?)(@sum.ba)$"

result = re.match(regex, eduid)

if result:
    print("Uspjesno")
else:
    print("Neuspjesno")
