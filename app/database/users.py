from app.database.database import conn, cursor

def create_user(name, email, password):
    cursor.execute(
        """
        INSERT INTO users (name, email, password)
        VALUES (?, ?, ?)
        """,
        (name, email, password)
    )

    conn.commit()