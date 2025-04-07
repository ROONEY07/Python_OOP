s = "hello world"
# print(s.split('o',1))

"""
    # string.split(separator, maxsplit)
    
    separator (optional): Eta sei character ba string, jeta diye split kora hobe. Default holo space (' ').

    maxsplit (optional): Eta bole dey koto bar split korte hobe. Default holo -1, mane kono limit nai.
"""

sentence = "Hello world Python"
result = sentence.split()
# print(sentence)
# print()
# print(result)


                                                          
data = "apple,banana,cherry"
result = data.split(',')
# print(result)
# print(type(result))




sentence2 = "apple banana cherry grape"
result1 = sentence2.split(' ', 4)
# print(result1)

sentence3 = "Python programming"
result2 = sentence3.split('o')
print(result2)

