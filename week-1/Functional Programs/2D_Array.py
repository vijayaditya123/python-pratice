M = int(input("Enter the row: "))
N = int(input("Enter the col : "))
list1 = []

def printing(list1,M,N):
    for i in range(M):
        for j in range(N):
            print(list1[i][j],end=" ")
            
        print(" ")    
        

for i in range(M):
    list2 = []
    for j in range(N):
        inp = input("Enter the data : ")
        if inp.lower()=="true":
            list2.append(True)
        elif  inp.lower()=="false":
            list2.append(False)
        elif "." in inp:
            list2.append(float(inp))
        else:
            list2.append(int(inp))
                
    list1.append(list2) 
printing(list1,M,N)    
      



