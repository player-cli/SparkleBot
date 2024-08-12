import sqlite3


class DataBase:

    def __init__(self, table_name: str) -> None:
        self.table_name = table_name
        self.base = sqlite3.connect("./data.db")
        self.cursor = self.base.cursor()

    def _add(self, chat_id: int, user_id) -> None:
        pass

    def _remove(self, chat_id: int, user_id) -> None:
        pass

    def _get_list(self) -> list:
        pass

    def _ban(self, chat_id: int, user_id) -> None:
        pass