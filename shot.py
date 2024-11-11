from circleshape import CircleShape
import pygame


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def collide(self, other):
        return super().collide(other)

    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="white", radius=self.radius, center=self.position, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)
        