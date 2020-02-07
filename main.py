from pygame.draw import polygon
from pygame.draw import lines
import pygame
from pygame import Surface
from Environment import Environment
from Point import Point
#Hardcode shapes
pygame.init()
shape_1 = [Point(25,96), Point(25,72), Point(103,72),Point(103,96)]
shape_2 = [Point(108,49), Point(132,68), Point(115,84)]
shape_3 = [Point(162,58), Point(176,70), Point(176,90), Point(162,98), Point(145,90), Point(145,70)]
shape_4 = [Point(75,21), Point(86,60), Point(64,60)]
shape_5 = [Point(45,1), Point(64,26), Point(48,59), Point(22,53), Point(16,26)]
shape_6 = [Point(88,35), Point(88,3), Point(107,1), Point(122,15)]
shape_7 = [Point(125,4), Point(158,4), Point(158,55), Point(125,55)]
shape_8 = [Point(174,2), Point(184,12), Point(180,62), Point(163,10)]
surface = pygame.display.set_mode()
polygon(surface,100,[x.get_coordinates() for x in shape_1])
polygon(surface,100,[x.get_coordinates() for x in shape_2])
polygon(surface,100,[x.get_coordinates() for x in shape_3])
polygon(surface,100,[x.get_coordinates() for x in shape_4])
polygon(surface,100,[x.get_coordinates() for x in shape_5])
polygon(surface,100,[x.get_coordinates() for x in shape_6])
polygon(surface,100,[x.get_coordinates() for x in shape_7])
polygon(surface,100,[x.get_coordinates() for x in shape_8])


#Prepare environment, find path, prepare surface, and display.
environment = Environment(list_of_shapes=[shape_1, shape_2, shape_3, shape_4, shape_5, shape_6, shape_7, shape_8], start=Point(18,86), goal=Point(189,5))
path = environment.a_star()
lines(surface, 200, False, [x.get_coordinates() for x in path])
pygame.display.update()