import sqlite3

try:
    connection = sqlite3.connect('data/servers/user_cursed.db')
    cursor = connection.cursor()
except Exception as e:
    print(__file__)
    print(e)


def user_is_cursed(guild_id: int, user_id: int) -> bool:
    check = cursor.execute("""SELECT 1
                              FROM cursed
                              WHERE guild_id = ? AND user_id = ?""",
                           (guild_id, user_id)).fetchone()
    return check is not None


def count_cursed_users(guild_id: int) -> int:
    all_cursed = cursor.execute("""SELECT COUNT(*)
                                   FROM cursed
                                   WHERE guild_id = ?""",
                                (guild_id,)).fetchone()
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


def user_curse(guild_id: int, user_id: int) -> tuple:
    curse = cursor.execute("""SELECT curse
                              FROM cursed
                              WHERE guild_id = ? AND user_id = ?""",
                           (guild_id, user_id)).fetchone()
    return curse


if __name__ == '__main__':
    print(user_curse(849107195081654282, 231580977405624320))
    print(user_curse(1, 1))
