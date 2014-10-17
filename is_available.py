def is_available(move=None, snake1=None, snake2=None, food=None, data=None, board_width=None, board_height=None):
    unavailable_points = [snake1.head, snake2.head]
    unavailable_points.append(snake1.body)
    unavailable_points.append(snake2.body)
    unavailable_points.append([Point(x=i, y=board_height) for i in xrange(board_width)])
    unavailable_points.append([Point(y=i, x=board_width) for i in xrange(board_height)])
    unavailable_points.append([Point(x=i, y=0) for i in xrange(board_width)])
    unavailable_points.append([Point(y=i, x=0) for i in xrange(board_height)])

    if move == 'd' and Point(x=snake1.head.x, y=snake1.head.y+1) in unavailable_points:
        return False
    if move == 'u' and Point(x=snake1.head.x, y=snake1.head.y-1) in unavailable_points:
        return False
    if move == 'l' and Point(x=snake1.head.x-1, y=snake1.head.y) in unavailable_points:
        return False
    if move == 'r' and Point(x=snake1.head.x+1, y=snake1.head.y) in unavailable_points:
        return False
    return True

#example use
is_available(move='r', snake1, snake2, food, data, board_width, board_height)