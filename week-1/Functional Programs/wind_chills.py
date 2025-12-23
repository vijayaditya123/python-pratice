import math
t=40
v=60
def WindCills(t,v):
   w=35.74+0.6215*t+(0.4275*t-35.75)*math.pow(v,0.16)
   print(w)
WindCills(t,v)   


