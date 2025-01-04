import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroid_field = AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.Surface.fill(screen, "black")
        for obj in updatable:
            obj.update(dt)

        for obj in drawable:
            obj.draw(screen)

        for asteroid in asteroids:
            if asteroid.get_collisions(player):
                sys.exit("Game over!")

            for shot in shots:
                if asteroid.get_collisions(shot):
                    shot.kill()
                    asteroid.kill()

        pygame.display.flip()
        
        
        dt = clock.tick(60) / 1000 


if __name__ == "__main__":
    main()