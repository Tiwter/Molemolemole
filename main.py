import pygame
from pygame.locals import *
import gamelib
from Hole import Hole
from Mole import Mole

class MoleGame(gamelib.SimpleGame):
	BROWN = pygame.Color('brown')
	GREY = pygame.Color('grey')

	def __init__(self):
		super(MoleGame, self).__init__('Mole', MoleGame.BROWN)
		self.mole = Mole()
		self.holes = (Hole((150,150)),Hole((280,150)),Hole((410,150)),
		Hole((150,250)),Hole((280,250)),Hole((410,250)),
		Hole((150,350)),Hole((280,350)),Hole((410,350)))

	def init(self):
		super(MoleGame, self).init()

	def __handle_event(self):
		for event in pygame.event.get():
			if(event.type == pygame.MOUSEBUTTONDOWN):
				self.hit()

	def render(self, surface):
		for hole in self.holes:
			hole.render(surface)
		self.mole.render(surface)

	def update(self):
		self.mole.update(self.holes)

	def hit(self):
		mouse_pos = pygame.mouse.get_pos()
		if(mouse_pos[0] - self.mole.get_mole_pos[0]-64 <= 0 and self.mole.get_mouse_pos[0] - self.mole.get_mole_pos[0] >= 0) and \
		(mouse_pos[1] - self.mole.get_mole_pos[1]-64 <= 0 and self.mole.get_mouse_pos[1] - self.mole.get_mole_pos[1] >= 0):
			print 'hited'

def main():
	game = MoleGame()
	game.run()

if __name__ == '__main__':
	main()