class Line:
    def __init__(self, start, end, is_horizontal, count=0):
        self.start = start
        self.end = end
        self.is_horizontal = is_horizontal
        self.count = count

    def __str__(self):
        return '({}, {}) - ({}, {})'.format(*self.start, *self.end)

    def __repr__(self):
        return self.__str__()

    def intersect(self, line):
        if self.is_horizontal == line.is_horizontal:
            if self.is_horizontal and self.start[1] == line.start[1]:
                max_x_left = max(min(self.start[0], self.end[0]), min(
                    line.start[0], line.end[0]))
                min_x_right = min(max(self.start[0], self.end[0]), max(
                    line.start[0], line.end[0]))

                if max_x_left <= min_x_right:
                    y = self.start[1]
                    return [(max_x_left, y), (min_x_right, y)]

            elif (not self.is_horizontal) and self.start[0] == line.start[0]:
                max_y_down = max(min(self.start[1], self.end[1]), min(
                    line.start[1], line.end[1]))
                min_y_up = min(max(self.start[1], self.end[1]), max(
                    line.start[1], line.end[1]))

                if max_y_down <= min_y_up:
                    x = self.start[0]
                    return [(x, max_y_down), (x, min_y_up)]
            return []

        h_line = self if self.is_horizontal else line  # Horizontal Line
        v_line = line if self.is_horizontal else self  # Vertical Line

        v_line_x = v_line.start[0]
        h_line_min_x = min(h_line.start[0], h_line.end[0])
        h_line_max_x = max(h_line.start[0], h_line.end[0])
        if not (v_line_x >= h_line_min_x and v_line_x <= h_line_max_x):
            return []

        h_line_y = h_line.start[1]
        v_line_min_y = min(v_line.start[1], v_line.end[1])
        v_line_max_y = max(v_line.start[1], v_line.end[1])
        if not (h_line_y >= v_line_min_y and h_line_y <= v_line_max_y):
            return []

        return [(v_line_x, h_line_y)]


def find_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
