f = open("test1.txt","r")
x=0
while True:
    char = f.read(1)
    if char == "(":
        x+=1
    elif char == ")":
        x+=-1
    else:
        print(x)
        break
    

f.close
