# Docs

## Glossary

- RDBMS relational database management system
- SQL structured query language
- DB (PostGres, MySQL,SQLite)

### List: 
It is the simplest database for storing purposes
Often, when start coding, this is the simplest way to start with.

```python
entries = [
    {"content":"lorem ipsum 1"},
    {"content":"lorem ipsum 2"},
    {"content":"lorem ipsum 3"},
    {"content":"lorem ipsum 4"},
]

```

### SQLite

- Install the desktop viewer for SQLIte if you don't have PyCharm with DB: [https://sqlitebrowser.org/](https://sqlitebrowser.org/)
- has 5 types of data: Integer, Text, Blob, Real, Numeric
- comments in SQL:
```sql
-- This is a comment.
-- The line below is not a comment.
CREATE TABLE users (first_name TEXT, surname TEXT);
```
- Connecting to SQLite with sqlite3
```python
import sqlite3
connection = sqlite3. connect ( "data.db")
connection. execute( "CREATE TABLE entries (content TEXT. date TEXT):") # execute does not save to DB, you have to commit
# connection.close()
def close_connection():
    connection.close()
```
> You can open as many connection as you like
- Commit and rolling back: how can we commit?
You can use either `with connection:` or `connection.commit()`
If you use `connection.execute()` sqlite3 create a cursor for us.
- What is a cursor: 
A structure that allows us to traverse a result set; (like an arrow in the Terminal)
Database cursors allow the database to only load results.
When requested, while SQLite cursors loads all result, but help us to go over them more easily

- add_entry function
```python
def add_entry(entry_content, entry_date):
    with connection:
        # don't hardcode values or at least once at the beginning
        # connection.execute("INSERT INTO entries VALUES ('today I am learning sql','21-10-2021');")
        # don't do this, try avoid SQL attack'
        # connection.execute(f"-- INSERT INTO entries VALUES ('{entry_content}','{entry_date}');")
        # the right way to do it
        connection.execute("INSERT INTO entries VALUES (?,?);", (entry_content, entry_date))
```

- Fetch row(s)
`cursor.fetchone();` or `cursor.fetchall();`
- - If you don't want to access the string property for a row:
```python
def view_entries(entries):
    for entry in entries:
        # print(f"{entry['date']} \n {entry['content']}\n\n") # valid for list db...
        # in the DB, we don't use a dictionary but TUPLES,so indices must be integers or slices
        print(f"{entry[1]} \n {entry[0]}\n\n")
        # if you still want to use:
        # print(f"{entry['date']} \n {entry['content']}\n\n")
        # you need to use in db.py: connection.row_factory = sqlite3.Row
```

---
## RReference

[Python SQL guide](https://pysql.tecladocode.com/)
