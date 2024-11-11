import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    #### PRINTING ####
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #### SETUP ####
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    # add player to both groups must be before instantiating and players
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    astriod_field = AsteroidField()


    #### GAME LOOP ####
    while True:
        # make the `x` button quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # filling the screen must be before updating and drawing the player
        screen.fill(color="black")
        # player.update(dt)
        for i in updatable:
            i.update(dt)
        for d in drawable:
            d.draw(screen)

        # After the update step in your game loop, iterate over all of the objects in your asteroids group. Check if any of them collide with the player. If a collision is detected, the program should print Game over! and immediately exit the program.
        for astroid in asteroids:
            if astroid.collide(player):
                print("Game over!")
                return 

        # Add another collision check to the game loop. Loop over each asteroid, and for each asteroid, loop over each bullet. If a bullet and an asteroid collide, call the .kill() method on both objects to remove them from the game.
        # WHERE did we define .kill()?
        # The kill() method is a feature built-in to pygame; it will remove the object from all of its groups, so our game will stop drawing and updating it automatically.
        for astroid in asteroids:
            for bullet in shots:
                if astroid.collide(bullet):
                    astroid.split()
                    bullet.kill()
            
        # player.draw(screen)
        pygame.display.flip()

        # limiting the timeframe to 60 FPS
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
