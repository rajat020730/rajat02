import math
def Sphere_radius(r):
    vol=(4/3)*math.pi*r*r*r
    return vol
print("Enter the radius:")
r=float(input())
print(Sphere_radius(r))
