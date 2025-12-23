import math
input_num = int(input("Enter the number : "))
i =0
a= int(math.pow(2,31))
while i<input_num:
 
    result = int(math.pow(2,i))
    if result<=a:
          print(result)
          i +=1
    else:
      break  



