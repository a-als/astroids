from circleshape import CircleShape
import constants
import pygame
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def collide(self, other):
        return super().collide(other)

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return 
        angle = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(angle)
        velocity2 = self.velocity.rotate(-1*angle)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        astriod1 = Asteroid(self.position.x, self.position.y, new_radius)
        astriod2 = Asteroid(self.position.x, self.position.y, new_radius)
        astriod1.velocity = velocity1 * 1.2
        astriod2.velocity = velocity2 * 1.2

    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="white", radius=self.radius, center=self.position, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)
        