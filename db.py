import sqlite3

connection = sqlite3.connect("data.db")
# connection.row_factory = sqlite3.Row


def create_table():
    with connection:
        connection.execute("CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);")


def add_entry(entry_content, entry_date):
    with connection:
        # the right way to create a connection, to avoid SQL attack
        connection.execute("INSERT INTO entries VALUES (?,?);", (entry_content, entry_date))


def get_entries():
    # return connection.execute("SELECT * FROM entries;") # not so obvious you're getting a cursor back
    cursor = connection.execute("SELECT * FROM entries;")
    return cursor


def delete_table():
    with connection:
        connection.execute("DROP TABLE IF EXISTS entries;")
