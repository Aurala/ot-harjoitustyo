import pygame, sys
from pygame.locals import *
from services.universe_service import UniverseService
from time import sleep

def main():

    # Initialize Pygame
    pygame.init()
    FPS = 60
    FramePerSec = pygame.time.Clock()
    window = pygame.display.set_mode((80, 40))
    window.fill((255, 255, 255))
    pygame.display.set_caption("Game")

    # Initialize Outomaatti
    universe_service = UniverseService(80, 40, "rules.life")
    generation = 0
    #print("Sukupolvi:", generation, " " * 5, "Soluja:", universe_service.count_cells())
    #print("\nPaina Ctrl+C poistuaksesi...")

    # Glidereita
    glider = [[1, 0, 0], [0, 1, 1], [1, 1, 0]]
    universe_service.add_pattern(0, 0, glider)
    universe_service.add_pattern(10, 10, glider)
    universe_service.add_pattern(20, 20, glider)

    # Blinkereitä
    blinker = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
    universe_service.add_pattern(5, 20, blinker)
    universe_service.add_pattern(5, 25, blinker)
    universe_service.add_pattern(5, 30, blinker)

    # Glider gun
    glider_gun = \
        [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    universe_service.add_pattern(40, 5, glider_gun)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        window.fill((255, 255, 255))

        universe = universe_service.get_universe_as_list()
        for y in range(len(universe)):
            for x in range(len(universe[0])):
                if universe[y][x] == 1:
                    pygame.draw.line(window, (0, 0, 0), (x, y), (x, y))

        pygame.display.flip()

        FramePerSec.tick(FPS)

        universe_service.next_generation()
        generation += 1

if __name__ == "__main__":
    main()
