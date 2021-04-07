p = input()
x=0
y=0
for c in p:
    if c.islower():
        x=x+1
    elif c.isupper():
        y=y+1
    else:
        pass
print("UPPER CASE ", y)
print("LOWER CASE ", x)