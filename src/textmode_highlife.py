from os import system
from time import sleep
from services.universe_service import UniverseService

def main():

    universe_service = UniverseService(80, 40, "rules.highlife")
    generation = 0

    # Replikaattori
    replicator = \
        [[0, 0, 1, 1, 1],
         [0, 1, 0, 0, 1],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 1, 0],
         [1, 1, 1, 0, 0]]
    universe_service.add_pattern(35, 17, replicator)

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
