#Complete the fuction to return the swapped digits of a given two-digit-interger.
def swap_digits(num):
    decena= num // 10
    unidades = num % 10

    return str(unidades) + str(decena)
   
   
   
#Invoke the function with any two digit interger as its argument
print(swap_digits(79))

