print()
print("Welcome to the Program....")
print()

num_points = int(input("Enter number of polygon points ---> "))
print()
print("Enter x and y coordinates of each point seperated by space --->")
print()

points_x = []
points_y = []

for i in range(num_points):
    x, y = map(float, input("Polygon point-" + str(i+1) + "--->").split())
    points_x.append(x)
    points_y.append(y)

print()
print("Point\tx\ty")
print("---------------------")
for i in range (num_points):
    print(i+1,"\t","%.2f" % points_x[i],"\t","%.2f" % points_y[i])

print()
points_x.append(points_x[0])
points_y.append(points_y[0])

#Calculations
Ax = 0
for i in range(num_points):
    Ax += (points_x[i+1] + points_x[i]) * (points_y[i+1] - points_y[i])
Ax = Ax / 2

Sx = 0 
for i in range(num_points):
    Sx += (points_x[i+1] - points_x[i]) * ((points_y[i+1] ** 2) + (points_y[i] * points_y[i+1]) + (points_y[i] ** 2))
Sx = -(Sx / 6)

Sy = 0
for i in range(num_points):
    Sy += (points_y[i+1] - points_y[i]) * ((points_x[i+1] ** 2) + (points_x[i] * points_x[i+1]) + (points_x[i] ** 2))
Sy = Sy / 6

Ix = 0
for i in range(num_points):
    Ix += (points_x[i+1] - points_x[i]) * ((points_y[i+1] ** 3) + ((points_y[i+1] ** 2) * points_y[i]) + ((points_y[i] ** 2) * points_y[i+1]) + (points_y[i] ** 3))
Ix = -(Ix / 12)

Iy = 0
for i in range(num_points):
    Iy += (points_y[i+1] - points_y[i]) * ((points_x[i+1] ** 3) + ((points_x[i+1] ** 2) * points_x[i]) + ((points_x[i] ** 2) * points_x[i+1]) + (points_x[i] ** 3))
Iy = Iy / 12

Ixy = 0
for i in range(num_points):
    Ixy += (points_y[i+1] - points_y[i]) * ((points_y[i+1] * (3 * (points_x[i+1] ** 2) + (2 * points_x[i+1] * points_x[i]) + (points_x[i] ** 2))) + (points_y[i] * (3 * (points_x[i] ** 2) + (2 * points_x[i+1] * points_x[i]) + (points_x[i+1] ** 2))) )
Ixy = -(Ixy / 24)

xt = Sy / Ax
yt = Sx / Ax

Ixt = Ix - ((yt ** 2) * Ax)
Iyt = Iy - ((xt ** 2) * Ax)
Ixyt = Ixy + ( xt * yt * Ax)

# results

print()
print("Geometric characteristics --->")
print()


print("Ax :" + '{:>10}'.format("%.2f" % Ax))
print("Sx :" + '{:>10}'.format("%.2f" % Sx))
print("Sy :" + '{:>10}'.format("%.2f" % Sy))
print("Ix :" + '{:>10}'.format("%.2f" % Ix))
print("Iy :" + '{:>10}'.format("%.2f" % Iy))
print("Ixy :" + '{:>9}'.format("%.2f" % Ixy))
print("xt :" + '{:>10}'.format("%.2f" % xt))
print("yt :" + '{:>10}'.format("%.2f" % yt))
print("Ixt :" + '{:>9}'.format("%.2f" % Ixt))
print("Iyt :" + '{:>9}'.format("%.2f" % Iyt))
print("Ixyt :" + '{:>8}'.format("%.2f" % Ixyt))