from constants import LINE_WIDTH
from circleshape import CircleShape
import pygame
from logger import log_event
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20,50)
            new_asteroid_vector_1 = self.velocity.rotate(random_angle)
            new_asteroid_vector_2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            ast1 = Asteroid(self.position[0], self.position[1], new_radius)
            ast1.velocity = new_asteroid_vector_1 * 1.2
            ast2 = Asteroid(self.position[0], self.position[1], new_radius)
            ast2.velocity = new_asteroid_vector_2 * 1.2