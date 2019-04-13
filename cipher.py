'''
Given a ciphertext encrypted with Caesar cipher, find the corresponding plaintext.
Encryption in Caesar cipher is done by replacing each letter with a letter 3 positions to the left,
e.g. 'a' is replaced with 'x', 'b' with 'y', ..., 'd' with 'a' and so on.
You need to fill in a function that takes as input a string,
the cipher text and sets the output variable to the corresponding plaintext. The ciphertext contains only lowercase alphabets.
Input: nrfzh
Output: quick
'''


ip = "nrfzh"

op = []
str = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
l = len(ip)
j = 0
for i in range (0,l):
    j = str.index(ip[i]) + 3
    if (j >= 25):
        j = j - 26
    op.append(str[j])
print (op)

