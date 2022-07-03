# 크로아티아 알파벳

word = input()
alphabet = ['c=','c-','dz=','d-','lj','nj','s=','z=']
result = 0

for i in alphabet:
    if i in word:
        result += word.count(i)
        word = word.replace(i, " ")
word = word.replace(" ", "")
result += len(word)

print(result)

