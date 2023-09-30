# Input
s = input().strip()

word = "hello"
i = 0 

for char in s:
    if char == word[i]:
        i += 1  

    if i == len(word):
        print("YES")
        break
else:
    print("NO")
