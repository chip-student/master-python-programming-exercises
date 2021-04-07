p = input()
x=0
y=0
for c in p:
    if c.isdigit():
        x=x+1
    elif c.isalpha():
        y=y+1
    else:
        pass
print("Letters ", y)
print("Digits ", x)