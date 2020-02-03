pi = 3.14159

radius = int(input("input radius"))
circumference = 2*pi*radius
print("circumference is:" + str(circumference))
area = pi*radius**2
print("area is: " + str(area))


double_radius = radius*2
print("when radius is doubled:")
circumference_2r = 2*pi*double_radius
print("circumference is: " + str(circumference_2r))
print("circumference is " + str(circumference_2r/circumference) + " times larger!")
area_2r = pi*double_radius**2
print("area is: " + str(area_2r))
print("area is " + str(area_2r/area) + " times larger!")


