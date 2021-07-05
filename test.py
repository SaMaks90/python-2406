triangle_width = [10, 14, 22, 13, 15, 18, 4, 6]
triangle_height = [4, 5, 21, 32, 14, 11, 9, 10]
triangle_s = []
min_triangle_s = None
max_triangle_s = None

for i in range(len(triangle_width)):
    triangle_s.append(triangle_width[i] * triangle_height[i])

for element in triangle_s:
    if min_triangle_s == None and max_triangle_s == None:
        min_triangle_s, max_triangle_s = element, element
    if element > max_triangle_s:
        max_triangle_s = element
    elif element < min_triangle_s:
        min_triangle_s = element

print(f'Minimum S triangle: {min_triangle_s};\nMaximum S triangle: {max_triangle_s}.')