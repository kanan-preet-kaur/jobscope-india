from passlib.hash import bcrypt
from database.database import conn, cursor

def register_user(name, email, password):
    hashed_password = bcrypt.hash(password)

    cursor.execute(
        "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
        (name, email, hashed_password)
    )

    conn.commit()

def login_user(email, password):

    cursor.execute(
        "SELECT name, password FROM users WHERE email = ?",
        (email,)
    )

    user = cursor.fetchone()

    if user is None:
        return None

    name, hashed_password = user

    if bcrypt.verify(password, hashed_password):
        return name

    return None