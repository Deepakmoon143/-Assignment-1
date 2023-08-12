a, b = 0, 1
print(a, end=" ")
for i in range(50):
    a,b = b, a+b
    if b<=50:
        print(b, end=" ")
