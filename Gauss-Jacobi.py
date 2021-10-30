def findX(y,z):
    return (-y-z)/5+1

def findY(x,z):
    return (-3*x-z+6)/4

def findZ(x,y):
    return (-3*x-3*y)/6

x = 5/10
y = 0
z = 0

for i in range(4):
    xi = findX(y,z)
    yi = findY(x,z)
    zi = findZ(x,y)
    print(f"{i} ___ X: {xi:.5f} | Y: {yi:.5f} | Z: {zi:.5f}")
    x = xi
    y = yi
    z = zi