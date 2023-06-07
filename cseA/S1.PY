a=input("Enter a string")
b=len(a)
if(b%5==0):
    c=a[::-1]
    print(c)
    d=c.capitalize()
    print(d)
else:
    print("No output")