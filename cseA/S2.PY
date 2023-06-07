a=input("Enter a string")
b=a[0:2]
c=a[-2:]
d=b+c
if(len(d)<2):
    print("Empty string")
elif(b==c):
    print("invalid string")
else:
    print(d)