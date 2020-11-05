a = [20,10,40,33,1]
for i in range(len(a)):
    for j in range(len(a)):
        if a[i] > a[j]:
            a[i],a[j] = a[j],a[i]
print(a)

