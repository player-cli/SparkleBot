import sqlite3

class DataBase:

    def __init__(self, table_name: str) -> None:
        self.table_name = table_name
        self.base = sqlite3.connect("./data.db", check_same_thread=False)
        self.cursor = self.base.cursor()

    def _add(self, cid: int, uid) -> None:
        self.cursor.execute(f"INSERT INTO {self.table_name} (cid, uid) VALUES (?, ?)", (cid, uid))
        self.base.commit()

    def _remove(self, uid) -> None:
        self.cursor.execute(f"DELETE FROM {self.table_name} WHERE uid = (?)", (uid))
        self.base.commit()

    def _get_list(self) -> list:
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        row = self.cursor.fetchall()
        return [[x[1], x[2]] for x in row]

    def _ban(self, cid: int, uid) -> None:
        self.cursor.execute("INSERT INTO banned (cid, uid) VALUES (?,?)", (cid, uid))
        self.cursor.execute(f"DELETE FROM users WHERE uid = (?)", (uid))
        self.base.commit()