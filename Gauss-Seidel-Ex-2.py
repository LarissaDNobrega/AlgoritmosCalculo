def findX(y,z):
    return -y-z+2400

def findY(x,z):
    return (-x-4*z+2200)/2

def findZ(x,y):
    return (-x-3*y+1900)/9

x = 5/10
y = 0
z = 0

for i in range(100):
    x = findX(y,z)
    y= findY(x,z)
    z = findZ(x,y)
    print(f"{i+1} ___ X: {x:.5f} | Y: {y:.5f} | Z: {z:.5f}")