n = int(input("Enter the total numbers: "))
list1=[]
for i in range(n):
    inp=int(input("enter the number: "))
    list1.append(inp)
count=0
list1.sort()
for i in range(n):
    if i>0 and list1[i]==list1[i-1]:
         continue
    j=i+1

    k=len(list1)-1
    while j<k:
       if list1[i]+list1[j]+list1[k]==0:
           print(f"({list1[i]},{list1[j]},{list1[k]})")
           count+=1 
           j+=1
           k-=1
       elif list1[i]+list1[j]+list1[k]<0:  
                  j+=1       
       else:
            k-=1
print(count)
           
           
