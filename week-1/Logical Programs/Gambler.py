import random
stake=int(input("Enter the stake : "))
goal =int(input("Enter the goal : "))
n=int(input("Enter the times : "))
i=0
win=0
loss=0

while i< n:
    stak=stake
    while stak>0 and stak !=goal:
         result = random.choice([-1,1])
         stak += result         

    if  stak == goal:
        win +=1
    else:
        loss +=1    

    i +=1
         
print(win)
win_percentage = (win/(win+loss))*100
loss_percentage =(loss/(win+loss))*100
print(win_percentage)
print(loss_percentage)
