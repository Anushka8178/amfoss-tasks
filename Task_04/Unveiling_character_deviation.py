# Input
t = int(input())

for i in range(t):
    s = input()
    reference = "amfoss"
    count = 0

    for j in range(len(reference)):
        if s[j] != reference[j]:
            count = count+1

    print(count)
