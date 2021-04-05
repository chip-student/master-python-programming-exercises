#Complete the function to calculate how many hours and minutes are passed since midnight.
def hours_minutes(secs):

    minutos = round(secs // 60)
    hora = round(secs // 3600)
  
    return (hora, minutos)




#Invoke the funtion and pass any interger as its argument.
print(hours_minutes(3900))