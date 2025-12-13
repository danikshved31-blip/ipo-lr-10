from collision.collision import isCorrectRect
from collision.collision import isCollisionRect
from collision.collision import intersectionAreaRect
from collision.collision import intersectionAreawultiRect

print(isCorrectRect([(10, 10), (11, 11)]))

print(isCollisionRect([(-3.4, 1),(9.2, 10)], [(-7.4, 0),(13.2, 12)]))

print(intersectionAreaRect([(-3, 1), (9, 10)], [(-7, 0), (13, 12)]))


rectangles = [
    [(-3, 1), (9, 10)],  
    [(-7, 0), (13, 12)],  
    [(0, 0), (5, 5)],  
    [(2, 2), (7, 7)]
]

result = intersectionAreawultiRect(rectangles)
print(f"Уникальная площадь пересечения: {result}")
