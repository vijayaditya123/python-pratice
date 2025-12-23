year=int(input("Enter the number : "))

a= year
count =0
while a != 0 :
       count += 1
       a=a//10

if count != 4:
       print("not a vaild year")
else:
        if year%4 == 0:
              print("a leap year")  
        else:
              print("not a leap year")   



 
          
            