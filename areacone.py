import math
h=int(input("Enter height : "))
r=int(input("Enter radius : "))

area=math.pi*r*(r+math.sqrt(math.pow(h,2)+math.pow(r,2)))
print("Area of Cone : ",area)