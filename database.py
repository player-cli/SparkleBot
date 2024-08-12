import sqlite3

class DataBase:

    def __init__(self, table_name: str) -> None:
        self.table_name = table_name
        self.base = sqlite3.connect("./data.db", check_same_thread=False)
        self.cursor = self.base.cursor()

    def _add(self, chat_id: int, user_id) -> None:
        self.cursor.execute(f"INSERT INTO {self.table_name} (chat_id, user_id) VALUES (?, ?)", (chat_id, user_id))
        self.db.commit()

    def _remove(self, user_id) -> None:
        self.cursor.execute(f"DELETE FROM {self.table_name} WHERE user_id = (?)", (user_id))
        self.db.commit()

    def _get_list(self) -> list:
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        row = self.cursor.fetchall()
        return [[x[1], x[2]] for x in row]

    def _ban(self, chat_id: int, user_id) -> None:
        self.cursor.execute("""
            INSERT INTO banned (chat_id, user_id)
            SELECT chat_id, user_id
            FROM users
            WHERE user_id = (?)
            RETURNING *;
            DELETE FROM users
            WHERE user_id = (SELECT user_id FROM banned WHERE user_id = (?));
        """, (user_id, user_id))