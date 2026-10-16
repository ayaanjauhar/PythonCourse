for x in range (1,30,2):
    print(x, end=" ")
print()
for y in range(2,31,2):
    print(y, end=" ")
print()
for z in range(100, -1, -10):
    print(z, end=" ")
print()
s = 0
for a in range(21):
    if a%2==0:
        s=s-a
    else:
        s=s+a
print(s)
list = [2,34,56,3,23]
n = int(input("Enter a no. ="))
flag=False
for b in list :
    if b==n:
        flag=True
        break
if flag:
    print("found")
else:
    print("not found")