# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']
n = int(input())
a1 = []
for t in range(n):
    a1.append(int(input()))
#a1 = list(map(int, input().split()))
a2 = list(filter(lambda x: x >= 9, a1))
long_group = len(groups)
long_a2 = len(a2)
diff = long_group - long_a2
if diff > 0:
    for i in range(0,diff):
        a2.append(None)
groups_final = dict(zip(groups, a2))
print(groups_final)




