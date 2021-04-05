#Complete the function to return:
#1) How many apples each single student will get.
#2) How many apples wil remain in the basket.
#Hint: You can resolve this exercise either importing the math module or without it 
def apple_sharing(n,k):

    student = round((k / n))
      
    return (student, k % n)
 
    
estudiantes = 6
manzanas = 50
#Print the two answer per the example output.
print(apple_sharing(estudiantes, manzanas))