#Input
n = int(input())
t = list(map(int, input().split()))
#Finding the minimum value among the values of time entered
min_time = min(t)
#If the minimum value is repeated
if t.count(min_time) > 1:
    print("Still Aetheria")
else:
    print(t.index(min_time) + 1)
