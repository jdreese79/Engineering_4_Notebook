print("Quadratic Solver")
print("Enter the coefficients for ax^2 + bx + c = 0")

import math

def solveQuad(x,y,z):
    return[(math.pow(y, 2)-4*x*z)]

def findRoots():
    return[((-b-math.sqrt(math.pow(b, 2)-4*a*c))/(2*a)), ((-b+math.sqrt(math.pow(b, 2)-4*a*c))/(2*a))]

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))


d = solveQuad(a,b,c)[0]#math.pow(b, 2)-4*a*c

if d < 0:
    print("There are no real roots")

elif d == 0:
    x = (-b+math.sqrt(math.pow(b, 2)-4*a*c))/(2*a)
    
else:
    x1 = findRoots()[0]#(-b+math.sqrt(math.pow(b, 2)-4*a*c))/(2*a)
    x2 = findRoots()[1]#(-b-math.sqrt(math.pow(b, 2)-4*a*c))/(2*a)
    
arr = [x1, x2]
print(arr[0])
print(arr[1])
