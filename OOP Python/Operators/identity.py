a = [1,2,3,4]
b = [1,2,3,4]
print(a is b)  
# identity is operator check kore, duita object akoi kina
# ai duita value akoi holei tara alda alda memory allocation kore . tai a and b same na

x = "hello"
y = "hello"
print(x is y)

# Python string ke intern kore, mane same value er strings same memory reference kore, so a ar b ekoi memory location e thake.

"""

    Key Difference between ('is' and '=='):

    is: Check kore identity, mane ki duita variable ekoi object reference kore, ba ekoi memory location e thake.

    ==: Check kore equality, mane duita variable er value ki same kina.
    
"""              