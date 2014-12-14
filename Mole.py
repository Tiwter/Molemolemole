import pygame
from pygame.locals import *
from random import randint

class Mole(object):

	def __init__(self, pos=(-100,-100)):
		self.t = 1
		self.pos = pos
		self.image = pygame.image.load("mole.png")

	def set_mole_pos(self, pos):
		self.pos = pos

	def get_mole_pos(self):
		return self.pos

	def random_hole(self, holes):
		self.pos = holes[randint(0,8)].get_hole_pos()

	def render(self,surface):
		surface.blit(self.image, self.pos)

	def update(self,holes):
		self.t -= 1
		if (self.t <= 0):
			self.random_hole(holes)
			self.t = 100