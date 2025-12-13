class RectCorrectError(Exception):
    """Пользовательское исключение для некорректных прямоугольников"""
    pass

def isCorrectRect(points):
    if len(points) != 2:
        return False
    
    try:
        (x1, y1), (x2, y2) = points
        return x1 < x2 and y1 < y2
    except (ValueError, TypeError):
        return False
    
def isCollisionRect(points1, points2):
    if len(points1) != 2 and len(points2) != 2:
        return False

    try:
        (x1, y1), (x2, y2) = points1
        (x3, y3), (x4, y4) = points2

        if x1 == x2 and y1 == y2:
            raise RectCorrectError("1й прямоугольник некорректный")
        
        r1_left = min(x1, x2)
        r1_right = max(x1, x2)
        r1_bottom = min(y1, y2)
        r1_top = max(y1, y2)

        if r1_left == r1_right or r1_bottom == r1_top:
            raise RectCorrectError("1й прямоугольник некорректный")
        
        if x3 == x4 and y3 == y4:
            raise RectCorrectError("2й прямоугольник некорректный")
        
        r2_left = min(x3, x4)
        r2_right = max(x3, x4)
        r2_bottom = min(y3, y4)
        r2_top = max(y3, y4)

        return (r1_right > r2_left and 
                r2_right > r1_left and
                r1_top > r2_bottom and
                r2_top > r1_bottom)

    except (ValueError, TypeError):
        return False
    
def intersectionAreaRect(points1, points2):
    # Проверяем, что оба списка содержат ровно 2 точки
    if len(points1) != 2 or len(points2) != 2:
        raise ValueError("Каждый прямоугольник должен быть задан двумя точками")
    
    try:
        (x1, y1), (x2, y2) = points1
        (x3, y3), (x4, y4) = points2
        
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Первый прямоугольник некорректен: первая точка должна быть левым нижним углом, вторая - правым верхним")
        if x3 >= x4 or y3 >= y4:
            raise ValueError("Второй прямоугольник некорректен: первая точка должна быть левым нижним углом, вторая - правым верхним")

        r1_left = x1
        r1_right = x2
        r1_bottom = y1
        r1_top = y2
        
        r2_left = x3
        r2_right = x4
        r2_bottom = y3
        r2_top = y4

        x_left = max(r1_left, r2_left)
        x_right = min(r1_right, r2_right)
        y_bottom = max(r1_bottom, r2_bottom)
        y_top = min(r1_top, r2_top)
        
        if x_right > x_left and y_top > y_bottom:
            width = x_right - x_left
            height = y_top - y_bottom
            return width * height
        else:
            return 0
            
    except ValueError as e:
        raise ValueError(f"Некорректные данные: {e}")

def intersectionAreawultiRect(rectangles):

    if not rectangles:
        return 0
    
    if not isinstance(rectangles, list):
        raise RectCorrectError("Аргумент должен быть списком прямоугольников")

    if len(rectangles) == 1:
        rect = rectangles[0]
        if (not isinstance(rect, list) or len(rect) != 2 or 
            not isinstance(rect[0], tuple) or not isinstance(rect[1], tuple) or
            len(rect[0]) != 2 or len(rect[1]) != 2):
            raise RectCorrectError("Прямоугольник должен быть списком из двух кортежей по два числа")
        
        (x1, y1), (x2, y2) = rect

        for coord in (x1, y1, x2, y2):
            if not isinstance(coord, (int, float)):
                raise RectCorrectError("Координаты должны быть числами")

        if x1 >= x2 or y1 >= y2:
            raise RectCorrectError("Прямоугольник некорректен: левая граница должна быть меньше правой, нижняя меньше верхней")
        
        return (x2 - x1) * (y2 - y1)

    try:
        first_rect = rectangles[0]
        if (not isinstance(first_rect, list) or len(first_rect) != 2 or 
            not isinstance(first_rect[0], tuple) or not isinstance(first_rect[1], tuple)):
            raise RectCorrectError("Каждый прямоугольник должен быть списком из двух кортежей")
        
        (x1, y1), (x2, y2) = first_rect
        
        for coord in (x1, y1, x2, y2):
            if not isinstance(coord, (int, float)):
                raise RectCorrectError("Координаты должны быть числами")
        
        if x1 >= x2 or y1 >= y2:
            raise RectCorrectError("Первый прямоугольник некорректен")
        
        current_x_left = x1
        current_x_right = x2
        current_y_bottom = y1
        current_y_top = y2
        
        for i in range(1, len(rectangles)):
            rect = rectangles[i]
            
            if (not isinstance(rect, list) or len(rect) != 2 or 
                not isinstance(rect[0], tuple) or not isinstance(rect[1], tuple) or
                len(rect[0]) != 2 or len(rect[1]) != 2):
                raise RectCorrectError(f"Прямоугольник {i} должен быть списком из двух кортежей по два числа")
            
            (x3, y3), (x4, y4) = rect
            
            for coord in (x3, y3, x4, y4):
                if not isinstance(coord, (int, float)):
                    raise RectCorrectError(f"Прямоугольник {i}: координаты должны быть числами")
            
            if x3 >= x4 or y3 >= y4:
                raise RectCorrectError(f"Прямоугольник {i} некорректен: левая граница должна быть меньше правой, нижняя меньше верхней")
            
            x_left = max(current_x_left, x3)
            x_right = min(current_x_right, x4)
            y_bottom = max(current_y_bottom, y3)
            y_top = min(current_y_top, y4)

            if x_right > x_left and y_top > y_bottom:
                current_x_left = x_left
                current_x_right = x_right
                current_y_bottom = y_bottom
                current_y_top = y_top
            else:
                return 0

        width = current_x_right - current_x_left
        height = current_y_top - current_y_bottom
        
        return width * height
        
    except (ValueError, TypeError) as e:
        if isinstance(e, (ValueError, TypeError)):
            raise RectCorrectError(f"Ошибка в данных: {e}")
        raise
