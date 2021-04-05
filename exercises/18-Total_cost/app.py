#Complete the function to return the total cost in dollars and cents of N cupcakes. 
#Remember you can return multiple parameters => return a, b
def total_cost(d,c,n):

    ckdol = n * d
    ckcen = n * c

    return ckdol, ckcen
    



#Invoke the function with three intergers: cost(dollars and cents) & number of cupcakes.
print(total_cost(10, 15, 2))
