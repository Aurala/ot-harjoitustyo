from os import system
from time import sleep
from services.outomaatti_service import OutomaattiService


def main():

    outomaatti = OutomaattiService(80, 40, "rules.highlife")
    generation = 0

    # Replikaattori
    replicator = \
        [[0, 0, 1, 1, 1],
         [0, 1, 0, 0, 1],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 1, 0],
         [1, 1, 1, 0, 0]]
    outomaatti.add_pattern(35, 17, replicator)

    while True:
        system("clear")
        print(outomaatti.get_universe_as_text())
        print("Sukupolvi:", generation, " " * 5,
              "Soluja:", outomaatti.count_cells())
        print("\nPaina Ctrl+C poistuaksesi...")
        sleep(1)
        outomaatti.next_generation()
        generation += 1


if __name__ == "__main__":
    main()
