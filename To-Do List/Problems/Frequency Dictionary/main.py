# put your python code here
a = list(input().lower().split())
d = {i: a.count(i) for i in set(a)}

'''for k, v in d.items():
    print(k, v)'''


print(*pair for pair in d.items())
    #print(*pair)