#Complete the function to return the first digit to the right of the decimal point.
def first_digit(num):
    result = str(num)
    for i in range(len(result)):
        if result[i] == '.':
            return int(result[i + 1])

#Invoke the function with a positive real number. ex. 34.33
print(first_digit(1.79))