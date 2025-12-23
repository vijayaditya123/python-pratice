N = int(input("enter the number: "))
i=1
result =0.0
if N==0:
    print("N cannot be zero")
else:    
    while i<=N:
     result +=float(1/i)
     i+=1
print(result)    



