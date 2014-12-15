import pygame
from pygame.locals import *
import gamelib
from Hole import Hole
from Mole import Mole
GREY = pygame.Color('grey')

class MoleGame(gamelib.SimpleGame):
	BROWN = pygame.Color('brown')
	GREY = pygame.Color('grey')

	def __init__(self):
		super(MoleGame, self).__init__('Mole', MoleGame.BROWN)
		self.mole = Mole()
		self.time = 1800
		self.score = 0
		self.time2 = 0
		self.holes = (Hole((150,150)),Hole((280,150)),Hole((410,150)),
		Hole((150,250)),Hole((280,250)),Hole((410,250)),
		Hole((150,350)),Hole((280,350)),Hole((410,350)))

	def init(self):
		global font
		super(MoleGame, self).init()
		font = pygame.font.SysFont("monospace", 20)
		self.render_score()

	def __handle_event(self):
		for event in pygame.event.get():
			if (event.type == QUIT) or \
                           (event.type == KEYDOWN and event.key == K_ESCAPE):
				self.terminate()
			if(event.type == pygame.MOUSEBUTTONDOWN):
				if(self.is_hit(self.mole)):
					self.mole_get_hit()

	def render_score(self):
		#global score_image
		self.score_image = font.render("Score = %d" % self.score, 0, GREY)

	def render(self, surface):
		global score_image
		surface.blit(self.score_image, (10,10))
		self.render_score()
		for hole in self.holes:
			hole.render(surface)
		self.mole.render(surface)

	def update(self):
		self.__handle_event()
		self.mole.update(self.holes)
		self.time += 1
		self.time2 = self.time/60
		print self.time2

	def mole_get_hit(self):
		self.mole.reset_mole_t()
		self.score += 1

	def is_hit(self, mole):
		mouse_pos = pygame.mouse.get_pos()
		mole_pos = mole.get_mole_pos()
		if(mouse_pos[0] - mole_pos[0] <= 64 and mouse_pos[0] - mole_pos[0] >= 0) and \
		(mouse_pos[1] - mole_pos[1] <= 64 and mouse_pos[1] - mole_pos[1] >= 0):
			return True
		return False

def main():
	game = MoleGame()
	game.run()

if __name__ == '__main__':
	main()
