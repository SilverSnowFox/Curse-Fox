import sqlite3

try:
    connection = sqlite3.connect('../data/servers/server_config.db')
    cursor = connection.cursor()
except sqlite3.Error:
    print("../data/servers/server_config.db doesn't exist or there was an error.")


def new_server(guild_id: int) -> None:
    cursor.execute("""INSERT INTO server_config(guild_id, all_can_cure)""", (guild_id, 1))
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
    return check == 1


def everyone_cure(guild_id: int, val: int):
    cursor.execute("""UPDATE server_config 
                      SET all_can_cure = ? 
                      WHERE guild = ?""",
                   (val, guild_id))


def can_everyone_cure(guild_id: int) -> bool:
    check = cursor.execute("""SELECT all_can_cure 
                              FROM server_config 
                              WHERE guild_id = ?""",
                           (guild_id,)).fetchone()
    return check[0] == 1

