from collision.collision import isCorrectRect
from collision.collision import isCollisionRect
from collision.collision import intersectionAreaRect
print(isCorrectRect([(10, 10), (11, 11)]))
print(isCollisionRect([(-3.4, 1),(9.2, 10)], [(-7.4, 0),(13.2, 12)]))
print(intersectionAreaRect([(-3, 1), (9, 10)], [(-7, 0), (13, 12)]))
print(intersectionAreaRect([(1, 1), (2, 2)], [(3, 17), (13, 1)]))
