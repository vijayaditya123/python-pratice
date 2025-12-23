import random
n = int(input("Enter the n: "))
list=[]
for i in range(n):
    list.append(i)
count=0
while len(list)!=0:
    count+=1
    num = random.randrange(0,n)
    if num in list:
        list.remove(num)
print(count)


