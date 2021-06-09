import sqlite3

try:
    connection = sqlite3.connect('data/servers/server_config.db')
    cursor = connection.cursor()
except Exception as e:
    print(__file__)
    print(e)


def new_server(guild_id: int) -> None:
    cursor.execute("""INSERT INTO server_config(guild_id, all_can_cure, all_can_curse)
                      VALUES (?, 1, 1)""", (guild_id,))
    connection.commit()


def delete_server(guild_id: int) -> None:
    cursor.execute("""DELETE FROM server_config 
                      WHERE guild_id = ?""",
                   (guild_id,))
    connection.commit()


def server_exists(guild_id: int) -> bool:
    check = cursor.execute("""SELECT 1 
                              FROM server_config 
                              WHERE guild_id = ?""",
                           (guild_id,)).fetchone()
    return check is not None


def everyone_cure(guild_id: int, val: int):
    cursor.execute("""UPDATE server_config 
                      SET all_can_cure = ? 
                      WHERE guild_id = ?""",
                   (val, guild_id))
    connection.commit()


def can_everyone_cure(guild_id: int) -> bool:
    check = cursor.execute("""SELECT all_can_cure 
                              FROM server_config 
                              WHERE guild_id = ?""",
                           (guild_id,)).fetchone()
    return check[0] == 1


def can_everyone_curse(guild_id: int) -> bool:
    check = cursor.execute("""SELECT all_can_curse
                              FROM server_config
                              WHERE guild_id = ?""",
                           (guild_id,)).fetchone()
    return check[0] == 1
