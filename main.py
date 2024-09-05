import sys
import pygame 
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Player.containers = (updatable,drawable)
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    dt = 0
    
    while (1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updatable:
            obj.update(dt)
            
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
    
        pygame.Surface.fill(screen, (0,0,0))
        
        for obj in drawable:
            obj.draw(screen)
            
        pygame.display.flip()
        
        #Limit Frame to 60FPS
        dt = fps.tick(60)/1000
        

if __name__ == "__main__":
    main()
