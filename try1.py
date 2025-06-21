try :
    number = int(input("Enter a number : "))
    result = 10 / number
except ValueError : 
    print("invaild input! Please enter a vaild number ")

except ZeroDivisionError:
    print("cannot divide a number by zero!")    

else:    


    print(f"The result is : {result}")
    print("This program ends here ")
    print("happy coding  ")


    