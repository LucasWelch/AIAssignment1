from Point import Point


class PointPathFValue:
    point = None
    path = []
    f_value = 0
    g_value = 0

    def __init__(self, point, old_path, f_value, g_value):
        self.point = point
        self.path = old_path
        self.path.append(self.point)
        self.f_value = f_value
        self.g_value = g_value

    def get_point(self):
        return self.point
