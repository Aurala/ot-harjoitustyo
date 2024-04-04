from os import system
from time import sleep
from services.outomaatti_service import OutomaattiService

def main():

    outomaatti = OutomaattiService(80, 40, "rules.life")
    generation = 0

    # Glidereita
    glider = [[1, 0, 0], [0, 1, 1], [1, 1, 0]]
    outomaatti.add_pattern(0, 0, glider)
    outomaatti.add_pattern(10, 10, glider)
    outomaatti.add_pattern(20, 20, glider)

    # Blinkereitä
    blinker = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
    outomaatti.add_pattern(5, 20, blinker)
    outomaatti.add_pattern(5, 25, blinker)
    outomaatti.add_pattern(5, 30, blinker)

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
    outomaatti.add_pattern(40, 5, glider_gun)

    while True:
        system("clear")
        print(outomaatti.get_universe_as_text())
        print("Sukupolvi:", generation, " " * 5, "Soluja:", outomaatti.count_cells())
        print("\nPaina Ctrl+C poistuaksesi...")
        sleep(1)
        outomaatti.next_generation()
        generation += 1

if __name__ == "__main__":
    main()
