import sqlite3

connection = sqlite3.connect('data/servers/server_config.db')
cursor = connection.cursor()


def new_server(guild_id: int) -> None:
    cursor.execute("INSERT INTO server_config(guild_id, agreed, all_can_cure)", (guild_id, False, False))
    connection.commit()


def delete_server(guild_id: int) -> None:
    cursor.execute("DELETE FROM server_config WHERE guild_id = ?", (guild_id,))
    connection.commit()


def check_agreed(guild_id: int) -> bool:
    return cursor.execute("SELECT agreed FROM server_config WHERE guild_id = ?", (guild_id,)).fetchone()


def has_agreed(guild_id: int) -> None:
    cursor.execute("UPDATE server_config SET agreed = ? WHERE guild_id = ?", (True, guild_id,))
    connection.commit()


def server_exists(guild_id: int) -> bool:
    check = cursor.execute("SELECT COUNT(1) FROM server_config WHERE guild_id = ?", (guild_id,))
    return bool(check)

