def isCorrectRect(points):
    if len(points) != 2:
        return False
    
    try:
        (x1, y1), (x2, y2) = points
        return x1 < x2 and y1 < y2
    except (ValueError, TypeError):
        return False
