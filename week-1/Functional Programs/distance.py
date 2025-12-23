import  math
x = int(input("Enter the x:"))
y =  int(input("Enter the y:"))
def Euclidean(x,y):
  x=x*x
  y=y*y
  dis =math.sqrt(x+y)
  print(f"the Euclidean distance {dis}")

Euclidean(x,y)



