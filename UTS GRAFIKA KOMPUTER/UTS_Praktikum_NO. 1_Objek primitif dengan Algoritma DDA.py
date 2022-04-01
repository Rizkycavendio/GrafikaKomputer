# Muhammad Rizky Cavendio - 20051397011
# UTS - Grafika Komputer

print("Masukkan nilai x1: ")
x1 = int(input())
print("Masukkan nilai x2: ")
x2 = int(input())
print("Masukkan nilai y1: ")
y1 = int(input())
print("Masukkan nilai y2: ")
y2 = int(input())


def ROUND(a):

  return int(a + 0.5)

dx = x2 - x1
dy = y2 - y1

m = dy/dx
if (dx > dy):
    steps = abs(dx)
    print()
    print("m < 1, sumbu x naik")
else:
    steps = abs(dy)
    print()
    print("m > 1, sumbu y naik")

xincrement = dx/steps
yincrement = dy/steps


for i in range(0,steps-1):
    x1 = x1 + xincrement
    y1 = y1 + yincrement

    print('{:2d} \t{:5d}, \t{:2.4f} \t{:3d} {:3d} \t{:2.3f} ({}, {})'.format(
        i, ROUND(x1), y1, dx, dy, m,ROUND(x1), ROUND(y1)))