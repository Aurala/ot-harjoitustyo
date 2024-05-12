from database_connection import get_database_connection
from config import settings
from repositories.library_repository import LibraryRepository


def drop_tables(connection):
    """Empties the database by dropping every table.

    Args:
        connection (sqlite3.Connection): Connection to SQLite3 database
    """

    sql_commands = [
        "DROP TABLE IF EXISTS Patterns",
        "DROP TABLE IF EXISTS Categories",
    ]

    cursor = connection.cursor()
    for command in sql_commands:
        cursor.execute(command)
    connection.commit()


def create_tables(connection):
    """Creates the database tables.

    Args:
        connection (sqlite3.Connection): Connection to SQLite3 database
    """
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


# Text source: https://conwaylife.com/wiki/Category:Patterns
# License: GNU Free Documentation License (https://www.gnu.org/licenses/fdl-1.3.html)

def populate_tables(connection):
    """Populates the database with categories and patterns.

    Args:
        connection (sqlite3.Connection): Connection to SQLite3 database
    """

    sql_command = """
                   INSERT INTO Categories (name, description) VALUES (?, ?)
                   """

    categories = [
        ["Käyttäjän tuomat",
         """
         Tässä kategoriassa ovat kaikki käyttäjän ohjelmaan tuomat kuviot.
         """,
         []
         ],
        ["Konduiitit (Conduits)",
         """
         Tähän kategoriaan kuuluu kuvioita, jotka pystyvät siirtämään aktiivisen
         reaktion toiseen paikkaan tulematta itse pysyvästi vahingoitetuiksi.
         """,
         ["conduit1.rle",
          "bx222.rle",
          "syringe.rle"]
         ],
        ["Eedenin puutarhat (Gardens of Eden)",
         """
         Sellaisia kuvioita, jotka eivät syntyä mistään muista kuvioista,
         kutsutaan Eedenin puutarhoiksi.
         """,
         ["gardensofeden2009.rle"]
         ],
        ["Pyssyt (Guns)",
         """
         Pyssy on paikallaan oleva kuvio, joka lähettää jatkuvasti
         matkaan avaruusaluksia.
         """,
         ["bigun.rle",
          "gosper_glider_gun.rle",
          "medusa.rle",
          "period44mwssgun.rle",
          "simkinglidergun.rle"]
         ],
        ["Metusalehit (Methuselahs)",
         """
         Metusalehit ovat kuvioita, joiden stabiloituminen kestää suuren
         määrän sukupolvia. Metusaleheista tulee jossain evoluutionsa
         vaiheessa paljon suurempia kuin mitä ne ovat alussa.
         """,
         ["queenbee.rle",
          "wing.rle",
          "52513m.rle"]
         ],
        ["Oskillaattorit (Oscillators)",
         """
         Oskillaattori on kuvio, joka toistaa säännöllistä evoluutiota eli
         se palaa tietyn sukupolvimäärän jälkeen lähtötilaansa.
         """,
         ["blinker.rle",
          "pulsar.rle",
          "pinwheel.rle",
          "p81_180_glider_loop.rle"]
         ],
        ["Tupruttajat (Puffers)",
         """
         Tupruttaja on kuvio, joka liikkuu kuin avaruusalus, mutta
         jättää jälkeensä jälkiä.
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
        ["Replikaattorit (Replicators)",
         """
         Replikaattori on kuvio, joka tuottaa mielivaltaisen
         määrän kopioita itsestään.
         """,
         ["replicator.rle"]
         ],
        ["Avarusalukset (Spaceships)",
         """
         Avaruusalus on kuvio, joka toistaa säännöllistä evoluutiota,
         mutta - toisin kuin oskillaattori - se liikkuu paikasta toiseen.
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
        ["Muuttumattomat (Still lifes)",
         """
         Muuttumattomat ovat kuvioita, jotka eivät muutu sukupolvesta toiseen.
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
        ["Sydänlangat (Wicks)",
         """
         Sydänlanka on staattinen tai oskilloiva lineaarisesti toistuva kuvio.
         """,
         ["ants.rle",
          "blinkerfuse.rle"]
         ],
    ]

    library_repository = LibraryRepository()

    cursor = connection.cursor()
    for category in categories:
        category_id = cursor.execute(
            sql_command, [category[0], category[1]]).lastrowid
        for filename in category[2]:
            library_repository.import_pattern(settings.resources.directory_patterns +
                                              filename, category_id=category_id)
    connection.commit()


def initialize_database():
    """Initializes the database."""

    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)
    populate_tables(connection)


if __name__ == "__main__":

    initialize_database()
