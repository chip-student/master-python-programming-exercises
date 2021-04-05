# Your code here

def fact(x):
    facto_total= 1
    while x > 1:
        facto_total *= x
        x -= 1
    return facto_total

x=int(input())
print(fact(x))