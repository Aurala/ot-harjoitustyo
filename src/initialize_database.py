import json
from database_connection import get_database_connection
from config import settings
from repositories.decoders.rle import RLE


def drop_tables(connection):

    sql_commands = [
        "DROP TABLE IF EXISTS Patterns",
        "DROP TABLE IF EXISTS Categories",
    ]

    cursor = connection.cursor()
    for command in sql_commands:
        cursor.execute(command)
    connection.commit()


def create_tables(connection):

    sql_commands = [
        """
        CREATE TABLE Patterns (
            pattern_id INTEGER PRIMARY KEY, 
            category_id INTEGER REFERENCES Categories,
            name TEXT,
            rules TEXT,
            pattern TEXT,
            metadata TEXT
        )
        """,
        """
        CREATE TABLE Categories (
            category_id INTEGER PRIMARY KEY,
            name TEXT,
            description TEXT
        )
        """
    ]

    cursor = connection.cursor()
    for command in sql_commands:
        cursor.execute(command)
    connection.commit()


def populate_tables(connection):

    decoder = RLE()

    sql_command1 = """
                   INSERT INTO Categories (name, description) VALUES (?, ?)
                   """
    sql_command2 = """
                   INSERT INTO Patterns (
                       category_id,
                       name,
                       rules,
                       pattern,
                       metadata
                   ) VALUES (?, ?, ?, ?, ?)
                   """

    # FIX: Translate the categories/descriptions (if Finnish terms exist)
    # Source: https://conwaylife.com/wiki/Category:Patterns
    # License: GNU Free Documentation License (https://www.gnu.org/licenses/fdl-1.3.html)

    categories = [
        ["Käyttäjän tuomat",
         """
         Tässä kategoriassa ovat kaikki käyttäjän ohjelmaan tuomat kuviot
         """,
         []
         ],
        ["Conduits",
         """
         This category contains conduits, arrangements of still lifes and/or
         oscillators that move an active reaction to another location without
         themselves being permanently damaged.
         """,
         ["conduit1.rle",
          "bx222.rle",
          "syringe.rle"]
         ],
        ["Garden of Eden",
         """
         A Garden of Eden is a pattern that has no parents and thus can only
         occur in generation 0.
         """,
         ["gardensofeden2009.rle"]
         ],
        ["Guns",
         """
         A gun is a stationary pattern that emits spaceships (or rakes)
         repeatedly forever.
         """,
         ["bigun.rle",
          "gosper_glider_gun.rle",
          "medusa.rle",
          "period44mwssgun.rle",
          "simkinglidergun.rle"]
         ],
        ["Methusalehs",
         """
         A methuselah is a pattern that takes a large number of generations
         in order to stabilize (known as its lifespan) and becomes much larger
         than its initial configuration at some point during its evolution.
         """,
         ["queenbee.rle",
          "wing.rle",
          "52513m.rle"]
         ],
        ["Oscillators",
         """
         An oscillator is a pattern that is a predecessor of itself. That is,
         it is a pattern that repeats itself after a fixed number of generations
         (known as its period).
         """,
         ["blinker.rle",
          "pulsar.rle",
          "pinwheel.rle",
          "p81_180_glider_loop.rle"]
         ],
        ["Puffers",
         """
         A puffer is a pattern that moves like a spaceship but leaves debris
         behind as it moves.
         """,
         ["puffer1.rle",
          "puffer2.rle",
          "blinkerpuffer1.rle",
          "blocklayingswitchengine.rle",
          "gliderproducingswitchengine.rle",
          "noahsark.rle",
          "pufferfish.rle",
          "p28blockpuffer.rle"]
         ],
        ["Replicators",
         """
         A replicator is any pattern that produces an arbitrary number of copies
         of itself. There is currently no precise definition.
         """,
         ["replicator.rle"]
         ],
        ["Spaceships",
         """
         A spaceship is a finite pattern that reappears (without additions or losses)
         after a fixed number of generations displaced by a non-zero amount.
         """,
         ["glider.rle",
          "bigglider.rle",
          "lwss.rle",
          "mwss.rle",
          "hwss.rle",
          "loafer.rle",
          "copperhead.rle",
          "bulldozer.rle",
          "lobster.rle",
          "enterprise.rle"]
         ],
        ["Still lifes",
         """
         A still life is a pattern that does not change from one generation to the next,
         and thus is a parent of itself.
         """,
         ["aircraftcarrier.rle",
          "314.rle",
          "beehive.rle",
          "block.rle",
          "boat.rle",
          "eater1.rle",
          "eater2.rle",
          "loaf.rle",
          "pond.rle",
          "ship.rle",
          "snake.rle",
          "tub.rle"]
         ],
        ["Wicks",
         """
         A wick is a static or oscillating linearly repeating pattern.
         """,
         ["ants.rle",
          "blinkerfuse.rle"]
         ],
    ]

    cursor = connection.cursor()
    for category in categories:
        category_id = cursor.execute(
            sql_command1, [category[0], category[1]]).lastrowid
        for filename in category[2]:
            with open(settings.resources.directory_patterns +
                      filename, "r", encoding="UTF-8") as rle_file:
                rle_data = rle_file.readlines()
            encoded = decoder.decode(rle_data)
            if encoded is not None:
                cursor.execute(sql_command2, [
                               category_id,
                               encoded[0],
                               encoded[1],
                               json.dumps(encoded[2]),
                               encoded[3]])
    connection.commit()


def initialize_database():

    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)
    populate_tables(connection)


if __name__ == "__main__":

    initialize_database()
