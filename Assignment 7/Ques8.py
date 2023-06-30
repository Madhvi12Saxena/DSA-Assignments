'''You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true'''

def checkStraightLine(coordinates):
    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]
    initial_slope = (y2 - y1) / (x2 - x1)

    for i in range(2, len(coordinates)):
        x, y = coordinates[i]
        x_prev, y_prev = coordinates[i-1]
        current_slope = (y - y_prev) / (x - x_prev)

        if current_slope != initial_slope:
            return False

    return True
coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
is_straight_line = checkStraightLine(coordinates)

print(f"Is Straight Line: {is_straight_line}")