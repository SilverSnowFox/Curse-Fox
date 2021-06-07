import sqlite3

try:
    connection = sqlite3.connect('../data/servers/user_cursed.db')
    cursor = connection.cursor()
except sqlite3.Error:
    print("../data/servers/server_config.db doesn't exist or there was an error.")


def user_is_cursed(guild_id: int, user_id: int) -> bool:
    check = cursor.execute("""SELECT 1
                              FROM cursed
                              WHERE guild_id = ? AND user_id = ?""",
                           (guild_id, user_id)).fetchone()
    return check is not None


def all_cursed_users(guild_id: int) -> list:
    all_cursed = cursor.execute("""SELECT *
                                   FROM cursed
                                   WHERE guild_id = ?""",
                                (guild_id,)).fetchall()
    return all_cursed


def curse_user(guild_id: int, user_id: int, curse: str) -> None:
    cursor.execute("""INSERT INTO cursed
                      VALUES (?,?,?)""",
                   (guild_id, user_id, curse))
    connection.commit()


def cure_user(guild_id: int, user_id: int) -> None:
    cursor.execute("""DELETE FROM cursed
                      WHERE guild_id = ? AND user_id = ?""",
                   (guild_id, user_id))
    connection.commit()


def cure_server(guild_id: int) -> None:
    cursor.execute("""DELETE FROM cursed
                      WHERE guild_id = ?""",
                   (guild_id,))
    connection.commit()
