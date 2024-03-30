from os import system
from time import sleep
from services.universe_service import UniverseService

def main():

    universe_service = UniverseService(40, 20)
    generation = 0

    # Glider vasempaan yläkulmaan
    universe_service.add_cell(0, 0)
    universe_service.add_cell(1, 1)
    universe_service.add_cell(2, 1)
    universe_service.add_cell(0, 2)
    universe_service.add_cell(1, 2)

    # Blinker oikeaan yläkulmaan
    universe_service.add_cell(30, 3)
    universe_service.add_cell(30, 4)
    universe_service.add_cell(30, 5)

    while True:
        system("clear")
        print(universe_service.get_textual_presentation())
        print("Sukupolvi:", generation)
        print("\nPaina Ctrl+C poistuaksesi...")
        sleep(1)
        universe_service.next_generation()
        generation += 1

if __name__ == "__main__":
    main()
