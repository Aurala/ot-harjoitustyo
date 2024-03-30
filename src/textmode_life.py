from os import system
from time import sleep
from services.universe_service import UniverseService

def main():

    universe_service = UniverseService(80, 40, "rules.life")
    generation = 0

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
        system("clear")
        print(universe_service.get_textual_presentation())
        print("Sukupolvi:", generation, " " * 5, "Soluja:", universe_service.count_cells())
        print("\nPaina Ctrl+C poistuaksesi...")
        sleep(1)
        universe_service.next_generation()
        generation += 1

if __name__ == "__main__":
    main()
