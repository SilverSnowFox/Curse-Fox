import json


def jupdate(universe: dict, path: str) -> str:
    with open(path, "w+") as f:
        json.dump(universe, f, indent=4, ensure_ascii=False)
    f.close()
    return "JSON Updated"
