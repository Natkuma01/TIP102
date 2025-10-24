def convert_letter(s):
    res = [s]
    temp = ""
    number_of_alpha =  sum(1 for char in s if char.isalpha())

# loop through the string
# if the letter is alpha, if is lower case, change to upper case, add the string to res
# if the letter is alpha, if is upper case, change to lower case, add the string to res
# 
 
    for char in s:
        if char.isalpha() and char.islower():
            temp += char.upper()

        elif char.isalpha() and char.isupper():
            temp += char.lower()

        else:
            temp += char
    res.append(temp)
    temp = ""
    return res

s = "a1b2"
print(convert_letter(s) )