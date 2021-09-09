import sqlite3

connect = sqlite3.connect('users.db')
cursor = connect.cursor()


def users_db():
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        nickname VARCHAR(20),
        userCity TEXT,
        fullname TEXT,
        age INTEGER,
        phone NUMERIC,
        email TEXT,
        effective TEXT,
        carModel TEXT,
        carColor TEXT,
        carNumber INTEGER,
        carDate INTEGER,
        engineVolume INTEGER
    )
    """)

    connect.commit()

    users_list = []
    cursor.execute("INSERT INTO users VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?);", users_list)
    connect.commit()

    # INTEGER, REAL (10.5), TEXT


def delete_db():
    cursor.execute("DROP TABLE users")
    connect.commit()


def search_db():
    cursor.execute("SELECT * FROM users")
    all_results = cursor.fetchall()
    print(all_results[0][1])


users_db()