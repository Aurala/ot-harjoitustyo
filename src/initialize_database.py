from database_connection import get_database_connection


def drop_tables(connection):

    sql_commands = [
        "DROP TABLE IF EXISTS Patterns",
        "DROP TABLE IF EXISTS Categories",
        "DROP TABLE IF EXISTS Rules"
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
            rules_id INTEGER REFERENCES Rules,
            name TEXT,
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
        """,
        """
        CREATE TABLE Rules (
            rule_id INTEGER PRIMARY KEY,
            name TEXT,
            description TEXT
        )
        """
    ]

    cursor = connection.cursor()
    for command in sql_commands:
        cursor.execute(command)
    connection.commit()


def initialize_database():

    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":

    initialize_database()
