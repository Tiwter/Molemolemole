import pygame
from pygame.locals import *

BLACK = pygame.Color('black')
GREY = pygame.Color('grey')

class Hole(object):

	def __init__(self, pos, color = BLACK):
		self.pos = pos
		self.color = color

	def get_hole_pos(self):
		pos_temp = self.pos[0]+10,self.pos[1]-20
		return pos_temp

	def set_hole_pos(self, pos):
		self.pos = pos

	def render(self, surface):
		pygame.draw.ellipse(surface, self.color, (self.pos,(80,40)), 0)

	def update(self, surface):
		pass