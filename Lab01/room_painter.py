import math
COVERAGE = 400
length = int(input("what is the length of the room in feet?"))
width = int(input("what is the width of the room in feet?"))
height = int(input("what is the height of the room in feet?"))
coats = int(input("how many coats of paint do you want?"))

surface_area = height*width*2+length*height*2+length*width
coverage_needed = surface_area*coats
cans_of_paint_required = coverage_needed/COVERAGE

print("numbers of cans required:")
print(math.ceil(cans_of_paint_required))
