a = [1, 2 ,3,4]
for i in range (len (a)-1):
    print(a)
    count = 0
    for f in range (len(a)-i-1):
        if a[i]>a[i+1]:
            a[i],a[i+1] = a[i+1],a[i];
            count += 1
    
    if count == 0:
        break