
# import classes
from fullcontrol.combinations.gcode_and_visualize.classes import Point, Extruder
# objects are imported here with functionality for both gcode and visualization. this means
# the modules within the geometry subpackage can simply import from here, with the idea being
# that only one import command needs to be changed if a different combination of properties is
# used (i.e. this bit in the line above: fullcontrol.combinations.gcode_and_visualize.classes).
from fullcontrol.geometry.vector import Vector
from fullcontrol.geometry.polar import PolarPoint

# import functions
from fullcontrol.geometry.polar import point_to_polar, polar_to_point, polar_to_vector
from fullcontrol.geometry.midpoint import midpoint
from fullcontrol.geometry.measure import distance, angleXY_between_3_points, centreXY_from_3_points  # , distance_forgiving
from fullcontrol.geometry.move import move
from fullcontrol.geometry.move_polar import move_polar
from fullcontrol.geometry.perpendicular_vector import perpendicular_vectorXY, perpendicular_vectorXY_from_vector
from fullcontrol.geometry.intersect import intersectXY, intersectXY_from_vector
from fullcontrol.geometry.reflect import reflectXY, reflectXY_mc
from fullcontrol.geometry.reflect_polar import reflectXYpolar
from fullcontrol.geometry.ramping import ramp_xyz, ramp_polar
from fullcontrol.geometry.arcs import arcXY, variable_arcXY, elliptical_arcXY, three_point_arcXY
from fullcontrol.geometry.shapes import rectangleXY, circleXY, ellipseXY, polygonXY, spiralXY, helixZ
from fullcontrol.geometry.waves import squarewaveXY, squarewaveXYpolar, trianglewaveXYpolar, sinewaveXYpolar
from fullcontrol.geometry.segmented_line import segmented_line
from fullcontrol.geometry.travel_to import travel_to
