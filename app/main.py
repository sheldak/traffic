import pygame

from map_loader import load_map
from app.config import MAP_PATH

pygame.init()
pygame.display.set_caption("Traffic Simulation")
clock = pygame.time.Clock()

world_map = load_map(MAP_PATH)

time = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    world_map.update(time)

    pygame.display.flip()
    time += 1
    clock.tick(30)

pygame.quit()
