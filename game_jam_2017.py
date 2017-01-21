import pygame

pygame.init()

class Player(pygame.sprite.Sprite):
	def __init__(self, *groups):
		super(Player, self).__init__(*groups)
		self.image = pygame.image.load("player.png")
		self.rect = pygame.rect.Rect((320, 240), self.image.get_size())

	#def update(self):
	#def update(self, dt):
	def update(self, dt, game):
		# Take copy of our position
		last = self.rect.copy() 

		key = pygame.key.get_pressed()
		if key[pygame.K_LEFT]:
			#self.rect.x -= 10
			self.rect.x -= 300 * dt
		if key[pygame.K_RIGHT]:
			self.rect.x += 300 * dt
		if key[pygame.K_UP]:
			self.rect.y -= 300 * dt
		if key[pygame.K_DOWN]:
			self.rect.y += 300 * dt

		# Conforming collisions
		new = self.rect
		for cell in pygame.sprite.spritecollide(self, game.walls, False):
			#self.rect = last
			cell = cell.rect
			if last.right <= cell.left and new.right > cell.left:
				new.right = cell.left
			if last.left >= cell.right and new.left < cell.right:
				new.left = cell.right
			if last.bottom <= cell.top and new.bottom > cell.top:
				new.bottom = cell.top
			if last.top >= cell.bottom and new.top < cell.bottom:
				new.top = cell.bottom



# Reusable
class Game(object):
	def main(self, screen):
		clock = pygame.time.Clock()

	 	## start position	
	 	#image_x = 360
	 	#image_y = 240

		image = pygame.image.load('player.png')
		background = pygame.image.load("background.png")
		sprites = pygame.sprite.Group()
		self.player = Player(sprites)
		# Create Walls
		self.walls = pygame.sprite.Group()
		block = pygame.image.load("block.png")
		b_width = 32
		b_height = 32
		for x in range(0, 640, b_width):
			for y in range(0, 480, b_height):
				if x in (0, 640-b_width) or y in (0, 480-b_height):
				    wall = pygame.sprite.Sprite(self.walls)
				    wall.image = block
				    wall.rect = pygame.rect.Rect((x, y), block.get_size())
		sprites.add(self.walls) 



		while 1:
			# Timing
			#clock.tick(30)
			dt = clock.tick(30)
			

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return
				if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
					return



			#sprites.update()
			#sprites.update(dt / 1000.)
			sprites.update(dt/1000., self)

			#screen.fill((200, 200, 200))
			screen.blit(background, (0,0))
			#screen.blit(circle_image, (320, 240))
			#screen.blit(image, (320, 240))
			sprites.draw(screen)
			pygame.display.flip()

if __name__ == '__main__':
	pygame.init()
	screen = pygame.display.set_mode((640, 480))
	Game().main(screen)






"""
height = 480
width = 640
screen = pygame.display.set_mode((height, width))

# Main loop
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT():
			running = False
		if event.type == pygame.KEWDOWN and event.key == pygame.K_ESCAPE:
			running = False


		
		# SIIMPLE MOVEMENT

			#image_x += 1
			key = pygame.key.get_pressed()
			if key[pygame.K_LEFT]:
				image_x -= 10
			if key[pygame.K_RIGHT]:
				image_x += 10
			if key[pygame.K_UP]:
				image_y -= 10
			if key[pygame.K_DOWN]:
				image_y += 10


"""
