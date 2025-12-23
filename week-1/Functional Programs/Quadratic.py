import math
quadratic_equation="1*x*x-5*x+4"
a=1
b=-5
c=4
def quadratic(a,b,c):
    delta= b*b-4*a*c    
    root1 =(-b+math.sqrt(delta))/(2*a)
    root2 =(-b-math.sqrt(delta))/(2*a)
    print(root1)
    print(root2)

quadratic(a,b,c)    








