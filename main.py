import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main ():
	print ("Starting Asteroids!")
	print (f"Screen width: {SCREEN_WIDTH}")
	print (f"Screen height: {SCREEN_HEIGHT}")

	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	updatable.add(player)
	drawable.add(player)

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	Shot.containers = (shots, drawable, updatable)
	AsteroidField.containers = (updatable)
	asteroid_field = AsteroidField()

	while True:
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
        			return

		updatable.update(dt)

		for asteroid in asteroids:
			for shot in shots:
				if asteroid.collision(player):
					print ("Game over!")
					sys.exit()

		for shot in shots:
			for asteroid in asteroids:
				if asteroid.collision(shot):
					shot.kill()
					asteroid.split()

		screen.fill("black")

		for obj in drawable:
			obj.draw(screen)

		pygame.display.flip()
		dt = clock.tick(60) / 1000


if __name__ == "__main__":

	main()
