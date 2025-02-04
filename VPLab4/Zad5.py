string = input()
digits = list()
special = list()
letters = list()
special_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")","-", "+", "?", "_", "=","<", ">", "/"]

for i in string:
    if i.isdigit():
        digits.append(i)
    elif i in special_characters:
        special.append(i)
    else:
        letters.append(i)


print("".join(digits))
print("".join(letters))
print("".join(special))



