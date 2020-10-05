f = open("day1.txt","r")
y=0
x=0
while True:
    char = f.read(1)
    y+=1
    if char =="(":
        x+=1

    elif char ==")":
        x+=-1
        
    if x == -1:
        print(y)
        print(x)
        break
        
