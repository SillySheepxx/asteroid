import sys

import pygame
from constants import *
from player import *
from asteroid import Asteroid
from AsteroidField import AsteroidField
from shot import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    Player.containers = (updatables, drawables)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatables, drawables)


    AsteroidField.containers = updatables
    asteroField = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatables, drawables)


    while True:
        screen.fill(pygame.Color(0, 0, 0))
        for updatable in updatables:
            updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                #sys.exit()
            for shot in shots:
                if asteroid.check_collision(shot):
                    shot.kill()
                    asteroid.split()

        for drawable in drawables:
            drawable.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60)
        dt /= 1000
        pygame.display.flip()
if __name__ == "__main__":
    main()


