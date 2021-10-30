def findX(y,z):
    return (-y-z)/5+1

def findY(x,z):
    return (-3*x-z+6)/4

def findZ(x,y):
    return (-3*x-3*y)/6

x = 5/10
y = 0
z = 0

for i in range(5):
    x = findX(y,z)
    y= findY(x,z)
    z = findZ(x,y)
    print(f"{i+1} ___ X: {x:.5f} | Y: {y:.5f} | Z: {z:.5f}")