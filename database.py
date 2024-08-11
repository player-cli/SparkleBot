import sqlite3


class DataBase:

    def __init__(self, table_name: str) -> None:
        self.table_name = table_name

    def _add(self, username: str, chat_id: int, user_id) -> None:
        pass

    def _remove(self, username: str, chat_id: int, user_id) -> None:
        pass

    def _get_list(self) -> list:
        pass

    def _ban(self, username: str, chat_id: int, user_id) -> None:
        pass