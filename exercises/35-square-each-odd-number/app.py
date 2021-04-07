value = []
items=[x for x in input().split(',')]
for p in items:
    intp = int(p)
    if intp % 2 != 0:
        value.append(p)
print(','.join(value))