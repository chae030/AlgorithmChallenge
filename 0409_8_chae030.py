n = int(input())
d = input().split()
v = int(input())
k = 0

for i in range(len(d)) :
    if v == int(d[i]) :
        k += 1
        
print(k)