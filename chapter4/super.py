area = [[0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0]]

directions = (((0, -1), (0, 1)),
              ((-1, 0), (1, 0)),
              ((-1, -1), (1, 1)),
              ((1, -1), (-1, 1)))


def detect_in_line(row, col, dir, found):
    """Check how many ones are in given direction"""
    global area

    try:
        if area[row][col] is 0:
            return found
    except IndexError:
        # everyting out of the list is 0
        return found

    found += 1
    x, y = dir
    return detect_in_line(row + y, col + x, dir, found)


def check(row, col):
    """Checks if there are 4 ones in a line
    
    tries every direction from given cell"""
    global directions

    for dirs in directions:
        # sums ones in given line
        # |, -, \, /
        how_many = 0
        for dir in dirs:
            x, y = dir
            how_many += detect_in_line(row + y, col + x, dir, 0)
        if how_many >= 3:
            # if at least 3 ones found
            return True
    return False

if __name__ == '__main__':
    print(check(2, 2))
