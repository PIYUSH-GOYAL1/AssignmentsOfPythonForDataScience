# # SPLITTING OF STRNG INTO A LIST

s = "Hi there Class!"
list_1 = []
temp = ''
for char in s:
    if char == ' ':
        list_1.append(temp)
        temp = ''
    else:
        temp += char
if temp:
    list_1.append(temp)

print(list_1)