#Complete the function to return the tens digit of a given interger
def tens_digit(num):

    result = int((num / 10) % 10)

    return result




#Invoke the function with any interger.
print(tens_digit(179))