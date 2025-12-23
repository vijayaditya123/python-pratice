import random 
num_of_times =  int(input("Enter the num: "))
head=0
tail=0
i=0                                                                              
while i <num_of_times:
      a=random.random()
      if a<0.5:
            tail = tail+1
      else:
            head=head+1  
      i+=1       

print("the percentage of  head "+str(int(float(head/num_of_times) *100)))
print("the percentage of  tail "+str(int(float(tail/num_of_times) *100)))

