def move(snake1=None, snake2=None, food=None, data=None, board_width=None, board_height=None):
    from collections import namedtuple
    Point = namedtuple('Point', 'x y') # point instances

    def is_available(move=None, snake1=None, snake2=None, food=None, data=None, board_width=None, board_height=None):
        unavailable_points = []
        unavailable_points.extend(snake1.body)
        unavailable_points.extend(snake2.body)
        unavailable_points.extend([Point(x=i, y=board_height) for i in xrange(board_width)])
        unavailable_points.extend([Point(y=i, x=board_width) for i in xrange(board_height)])
        unavailable_points.extend([Point(x=i, y=-1) for i in xrange(board_width)])
        unavailable_points.extend([Point(y=i, x=-1) for i in xrange(board_height)])

        if move == 'd' and Point(x=snake1.head.x, y=snake1.head.y+1) in unavailable_points:
            return False
        if move == 'u' and Point(x=snake1.head.x, y=snake1.head.y-1) in unavailable_points:
            return False
        if move == 'l' and Point(x=snake1.head.x-1, y=snake1.head.y) in unavailable_points:
            return False
        if move == 'r' and Point(x=snake1.head.x+1, y=snake1.head.y) in unavailable_points:
            return False
        return True

    x_dst, y_dst = food.x - snake1.head.x, food.y - snake1.head.y
    if x_dst > 0 and is_available('r', snake1, snake2, food, data, board_width, board_height):
        return 'r'
    elif x_dst < 0 and is_available('l', snake1, snake2, food, data, board_width, board_height):
        return 'l'
    elif y_dst > 0 and is_available('d', snake1, snake2, food, data, board_width, board_height):
        return 'd'
    elif is_available('u', snake1, snake2, food, data, board_width, board_height):
        return 'u'
    elif is_available('r', snake1, snake2, food, data, board_width, board_height):
        return 'r'
    elif is_available('l', snake1, snake2, food, data, board_width, board_height):
        return 'l'
    return 'd'

    