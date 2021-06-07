import sqlite3
import json
from typing import List

try:
    connection = sqlite3.connect('../data/servers/server_curses.db')
    cursor = connection.cursor()
except sqlite3.Error:
    print("../data/servers/server_config.db doesn't exist or there was an error.")


def initiate_server(guild_id: int):
    # Start server with defaults
    try:
        with open("../data/initial_curses.json", "r") as f:
            initial = json.load(f)

            for cur in initial:
                cursor.execute("""INSERT INTO all_servers (guild_id,curse) 
                                  VALUES (?,?)""",
                               (guild_id, cur))
            connection.commit()
    except FileExistsError:
        print("default_curses.json doesn't exist.")


def curse_exists(guild_id: int, curse: str) -> bool:
    check = cursor.execute("""SELECT 1 
                              FROM all_servers 
                              WHERE guild_id = ? AND curse = ?""",
                           (guild_id, curse)).fetchone()
    return check is not None


def create_curse(guild_id: int, curse: str) -> None:
    cursor.execute("""INSERT INTO all_servers
                      VALUES (?,?)""",
                   (guild_id, curse))
    connection.commit()


def delete_curse(guild_id: int, curse: str) -> None:
    cursor.execute("""DELETE FROM all_servers
                      WHERE guild_id = ? AND curse = ?""",
                   (guild_id, curse))
    connection.commit()


def delete_server(guild_id: int) -> None:
    cursor.execute("""DELETE FROM all_servers
                      WHERE guild_id = ?""",
                   (guild_id,))
    connection.commit()
    # Removes all entries in cursed list
    import SQLUser_cursed
    SQLUser_cursed.cure_server(guild_id)


def get_all_curses(guild_id: int) -> List[tuple]:
    return cursor.execute("""SELECT curse 
                             FROM all_servers
                             WHERE guild_id = ?""", (guild_id,)).fetchall()


if __name__ == '__main__':
    # initiate_server(12)
    # delete_curse(12, "nya")
    print(get_all_curses(12))
