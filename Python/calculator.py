a = input("Enter first number: ")
b = input("Enter second number: ")



def doMath(x,y,z):
    x = int(x)
    y = int(y)
    if z == 1:
        return(str(x+y))
    if z == 2:
        return(str(x-y))
    if z == 3:
        return(str(x*y))
    if z == 4:
        return(str(round(x/y,2)))
    if z == 5:
        return(str(x%y))


print("Sum:\t\t" + doMath(a,b,1))
print("Difference:\t" + doMath(a,b,2))
print("Product:\t" + doMath(a,b,3))
print("Quotient:\t" + doMath(a,b,4))
print("Modulo:\t\t" + doMath(a,b,5))
