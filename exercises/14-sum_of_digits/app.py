#Complete the function "digits_sum" so that it prints the sum of a three digit number.
def digits_sum(num):
    suma=0
    result = str(num)
    for i in range(len(result)):
        suma += int(result[i])
    return suma


#Invoke the function with any three-digit-number
#You can try other three-digit numbers if you want
print(digits_sum(123))