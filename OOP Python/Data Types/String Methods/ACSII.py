# char to ascii 
str1 = 'z'
# print("Ascii value of A:",ord(str1))

# ascii to char
str2 = 57
str3 = 75
# print("char of str2 is:",chr(str2))
# print("char of str3 is:",chr(str3))




word = "kiara"
# print({char: ord(char) for char in word})
# print(chr(76))
# print(ord('A'))


for i in word:
    for char in i:
        print(f"{char}:{ord(char)}",sep="\n")