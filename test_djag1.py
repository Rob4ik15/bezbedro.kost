a = (input("напиши потато "))
b = int(0)
for i in range (len (a)):
    b += int(a [i]) * 2 **(len (a) -i -1)
print (b)