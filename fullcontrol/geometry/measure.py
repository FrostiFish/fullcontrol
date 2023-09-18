from fullcontrol.geometry import Point, point_to_polar, midpoint
from fullcontrol.geometry.perpendicular_vector import perpendicular_vectorXY
from fullcontrol.geometry.intersect import intersectXY_from_vector

def distance(point1: Point, point2: Point) -> float:
    'return distance between two points'
    return ((point1.x-point2.x)**2+(point1.y-point2.y)**2+(point1.z-point2.z)**2)**0.5


def distance_forgiving(point1: Point, point2: Point) -> float:
    'return distance between two points. x, y or z components are ignored unless defined in both points'
    dist_x = 0 if point1.x == None or point2.x == None else point1.x - point2.x
    dist_y = 0 if point1.y == None or point2.y == None else point1.y - point2.y
    dist_z = 0 if point1.z == None or point2.z == None else point1.z - point2.z
    return ((dist_x)**2+(dist_y)**2+(dist_z)**2)**0.5


def angleXY_between_3_points(start_point: Point, mid_point: Point, end_point: Point) -> float:
    'returns the angle from start_point to end_point, about mid_point'
    return(point_to_polar(end_point, mid_point).angle - point_to_polar(start_point, mid_point).angle)


def centreXY_from_3_points(start_point: Point, mid_point: Point, end_point: Point) -> Point:
    'returns the centre point of the arc through three points'
    #start_point is referred to as point A, mid_point as point B, end_point as point C
    line_ab_midpoint = midpoint(start_point, mid_point)
    line_ab_perpendicular_vector = perpendicular_vectorXY(start_point, mid_point)
    line_bc_midpoint = midpoint(mid_point, end_point)
    line_bc_perpendicular_vector = perpendicular_vectorXY(mid_point, end_point)

    return intersectXY_from_vector(line_ab_midpoint, line_ab_perpendicular_vector, line_bc_midpoint, line_bc_perpendicular_vector)
