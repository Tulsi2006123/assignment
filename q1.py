import math
radius = 42
angle_deg = 60

arc_length = (angle_deg / 360) * 2 * math.pi * radius

side = arc_length /  4
area = side * side

print("Side of square:", side)
print("Area of square:",area)