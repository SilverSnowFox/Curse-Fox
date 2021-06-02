import json


# Returns the dict in the json
def load_json(j_path: str) -> dict:
    with open(j_path, 'r') as f:
        new = json.load(f)
        return new


def new_section(universe: dict, guild_id: int) -> dict:
    # Adds a new section to the universe dict
    basic_into = {
        "curses": {
            "nya": "{} cursed by cats!",
            "woof": "Who let the dogs out?",
            "kon": "{} is cursed by foxes?",
            "bzz": "Looks like {} got stung by a magical bee",
            "gobble": "Is it Thanksgiving yet?",
            "quack": "The ducks have arrived, who knows when they'll be gone",
            "owo": "Uh oh, seems wike you awe in twoubwe",
            "rawr": "Seems like a tiger has come from the East",
            "awo": "Seems like it's a full-moon tonight"
        },
        "users": {}
    }
    universe[str(guild_id)] = basic_into
    return universe


def get_curses(universe: dict) -> str:
    new = ""
    for curse in universe['curses'].keys():
        new = new + "¬ " + curse + "\n"
    return new


def is_cursed(universe: dict, user: int) -> bool:
    all_users = universe.keys()
    if str(user) in all_users:
        return True
    return False


def clear_curse(universe: dict, user: int) -> None:
    all_users = universe['users']
    all_users.pop(str(user))


def curse_exists(curse: str, universe: dict) -> bool:
    if curse in universe["curses"].keys():
        return True
    return False


def curse_user(curse: str, universe: dict, member: int) -> str:
    universe["users"][str(member)] = curse
    return universe["curses"][curse]


def cursed_message(message: str, curse: str) -> str:
    from TextToOwO import text_to_owo
    if curse == "owo":
        return text_to_owo(message)
    elif curse == "nya":
        new_msg = ""
        i = 0
        while i < len(message)-1:
            if message[i:i+4] == "http":
                while i < len(message) and message[i:i+4] != ".com":
                    new_msg += message[i]
                    i += 1
                new_msg += message[i:i+4]
                i += 4
            elif (message[i] == "N") and (message[i + 1] in "AEIOU"):
                new_msg += "NY"
            elif (message[i] == "N") and (message[i + 1] in "aeiou"):
                new_msg += "Ny"
            elif (message[i] == "n") and (message[i + 1].lower() in "aeiou"):
                new_msg += "ny"
            else:
                new_msg += message[i]
            i += 1
        new_msg += " nya"
        return new_msg
    else:
        return message + " " + curse
