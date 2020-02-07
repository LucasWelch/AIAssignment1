from Point import Point
import heapq
from PointPathFValue import PointPathFValue
import math


class Environment:
    start = None
    goal = None
    shapes = [] #List of lists which contain Points

    def __init__(self, start=Point(x=0,y=0), goal=Point(40,40), list_of_shapes=[]):
         self.start = start
         self.goal = goal
         for shape in list_of_shapes:
             self.shapes.append(shape)

    def a_star(self):
        heap = []
        closed = []
        start_x = self.start.get_coordinates()[0]
        start_y = self.start.get_coordinates()[1]
        goal_x = self.goal.get_coordinates()[0]
        goal_y = self.goal.get_coordinates()[1]
        original_f_value = math.sqrt(math.pow(goal_x-start_x,2) + math.pow(goal_y - start_y, 2))
        heapq.heappush(heap, (original_f_value, PointPathFValue(point=self.start,old_path=[],f_value=original_f_value,g_value=0)))
        while len(heap) != 0:
            current = heapq.heappop(heap)[1]
            print(str(current.point.get_coordinates()[0]) + "," + str(current.point.get_coordinates()[1]))
            if current.point not in closed:
                if current.point == self.goal:
                    return current.path
                closed.append(current.point)
                old_g_value = current.g_value
                old_f_value = current.f_value
                path = current.path
                point = current.point
                list_of_candidates = self.get_candidate_points(point=point)
                print(list_of_candidates)
                for candidate in list_of_candidates:
                    if candidate not in closed:
                        distance_to_candidate = math.sqrt((point.get_coordinates()[0] - candidate.get_coordinates()[0]) ** 2 + (point.get_coordinates()[1] - candidate.get_coordinates()[1]) ** 2) #Use point and candidate
                        new_g_value = old_g_value + distance_to_candidate
                        new_path = path[:]
                        new_path.append(candidate)
                        #for point in new_path:
                            #print(str(point.get_coordinates()[0]) + "," + str(point.get_coordinates()[1]))
                        distance_to_goal = math.sqrt(math.pow(goal_x-candidate.get_coordinates()[0],2) + math.pow(goal_y-candidate.get_coordinates()[1],2))
                        new_f_value = new_g_value + distance_to_goal
                        point_path_f_value = PointPathFValue(point=candidate,old_path=new_path,f_value=new_f_value,g_value=new_g_value)
                        heapq.heappush(heap,(new_f_value,point_path_f_value))
        return None

    def get_candidate_points(self, point):
        candidate_list = []
        for shape in self.shapes:
            if point in shape:
                index = shape.index(point)
                candidate_list.append(shape[(index+1)%len(shape)])
                candidate_list.append(shape[index-1])
            else:
                unobstructed = True
                for test_point in shape:
                    unobstructed = True
                    for test_shape in self.shapes:
                        for i in range(0, len(test_shape)):
                            i2 = i - 1
                            if point != test_shape[i] and point != test_shape[i2] and test_point != test_shape[i] and test_point != test_shape[i2]:
                                if Environment.intersect(point, test_point, test_shape[i], test_shape[i2]):
                                    unobstructed = False
                                    break
                        if not unobstructed:
                            break
                    if unobstructed:
                        candidate_list.append(test_point)

        test_point = self.goal
        for test_shape in self.shapes:
            for i in range(0, len(test_shape)):
                i2 = i - 1
                if point != test_shape[i] and point != test_shape[i2] and test_point != test_shape[i] and test_point != \
                        test_shape[i2]:
                    if Environment.intersect(point, test_point, test_shape[i], test_shape[i2]):
                        print("returning")
                        return candidate_list
        candidate_list.append(self.goal)
        print("returning 2")
        return candidate_list

    @staticmethod
    def orientation(p, q, r):
        p_x = p.get_coordinates()[0]
        p_y = p.get_coordinates()[1]
        q_x = q.get_coordinates()[0]
        q_y = q.get_coordinates()[1]
        r_x = r.get_coordinates()[0]
        r_y = r.get_coordinates()[1]
        # p and q are part of the same line.
        value = (q_y - p_y) * (r_x - q_x) - (q_x - p_x) * (r_y - q_y)
        if value == 0:
            return 0
        if value > 0:
            return 1
        if value < 0:
            return 2

    @staticmethod
    def part_of_same_segment(p, q, r):
        p_x = p.get_coordinates()[0]
        p_y = p.get_coordinates()[1]
        q_x = q.get_coordinates()[0]
        q_y = q.get_coordinates()[1]
        r_x = r.get_coordinates()[0]
        r_y = r.get_coordinates()[1]

        if r_x <= max(p_x, q_x) and r_x >= min(p_x, q_x) and r_y <= max(p_y, q_y) and r_y >= min(p_y, q_y): return True
        return False

    @staticmethod
    def intersect(line1_point1, line1_point2, line2_point1, line2_point2):
        orientation_1 = Environment.orientation(line1_point1, line1_point2, line2_point1)
        orientation_2 = Environment.orientation(line1_point1, line1_point2, line2_point2)
        orientation_3 = Environment.orientation(line2_point1, line2_point2, line1_point1)
        orientation_4 = Environment.orientation(line2_point1, line2_point2, line1_point2)

        if orientation_1 != orientation_2 and orientation_3 != orientation_4: return True

        if orientation_1 == 0 and Environment.part_of_same_segment(line1_point1, line1_point2, line2_point1): return True
        if orientation_2 == 0 and Environment.part_of_same_segment(line1_point1, line1_point2, line2_point2): return True
        if orientation_3 == 0 and Environment.part_of_same_segment(line2_point1, line2_point2, line1_point1): return True
        if orientation_4 == 0 and Environment.part_of_same_segment(line2_point1, line2_point2, line1_point2): return True
        return False