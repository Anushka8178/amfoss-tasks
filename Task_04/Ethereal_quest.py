# Input
n = int(input())
sumx = 0
sumy = 0
sumz = 0

# Read and sum the force vectors
for i in range(n):
    x, y, z = map(int, input().split())
    sumx += x
    sumy += y
    sumz += z

# Check if the construct is stable or not
if sumx == 0 and sumy == 0 and sumz == 0:
    print("YES")
else:
    print("NO")
