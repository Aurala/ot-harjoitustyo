from database_connection import get_database_connection


def drop_tables(connection):

    sql_commands = [
        "DROP TABLE IF EXISTS patterns",
        "DROP TABLE IF EXISTS categories"
    ]


def create_tables(connection):

    sql_commands = [
        """
        CREATE TABLE patterns (
            id primary key, 
            category text,
            name text
            comments text,
            pattern text,
            meta text,
            x_coord integer,
            y_coord integer,
            rules text,
            hash text
        )
        """,
        """
        CREATE TABLE categories (
            id primary key,
            name, description
        )
        """
    ]


def initialize_database():

    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":

    initialize_database()
