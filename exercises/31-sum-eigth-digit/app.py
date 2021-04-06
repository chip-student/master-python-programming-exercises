valores = []
for i in range(1000, 3001):
    p=str(i)
    if (int(p[0])%2==0) and (int(p[1])%2==0) and (int(p[2])%2==0) and (int(p[3])%2==0):
        valores.append(p)
print(",".join(valores))