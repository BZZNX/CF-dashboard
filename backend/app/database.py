import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "cf.db"



def init_db():
    conn = sqlite3.connect(DB_PATH)


    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            handle TEXT,
            rating INTEGER,
            max_rating INTEGER
        )
    """)

    conn.commit()
    conn.close()

def update_db(handle, rating, max_rating):
    conn = sqlite3.connect(DB_PATH)

    conn.execute("""
        UPDATE users
        SET rating = ?, max_rating = ?
        WHERE handle = ?
    """, (rating, max_rating, handle))

    conn.commit()
    conn.close()


def add_handle(handle):
    conn = sqlite3.connect(DB_PATH)

    conn.execute("""
        INSERT INTO users (handle)
        SELECT ?
        WHERE NOT EXISTS (
            SELECT 1 FROM users WHERE handle = ?
        )
    """, (handle, handle))

    conn.commit()
    conn.close()
    
def get_saved_users():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    rows = conn.execute("""
        SELECT handle, rating, max_rating AS maxRating
        FROM users
        ORDER BY rating DESC
    """).fetchall()

    users = [dict(row) for row in rows]

    conn.close()
    return users
