def obrni_string(string):
    if len(string) == 0:
        return string
    else:
        return obrni_string(string[1:]) + string[0]


input = input("Unesite string koji zelite obrnuti: ")

print(obrni_string(input))
