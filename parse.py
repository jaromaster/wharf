import tomllib
from typing import Any


class Wharf():
    """ class to model wharf-file contents """
    manager: str = ""
    names: list[str] = []

    def __str__(self) -> str:
        return f"Wharf[manager=\"{self.manager}\", names={self.names}]"


def parse_toml(path: str) -> dict[str, Any]:
    """ parse toml file and return dict """

    parsed: dict[str, Any] = None

    try:
        file = open(path)
        parsed = tomllib.loads(file.read())
    except:
        print("could not open file")
        return parsed

    return parsed


def build_wharf(parsed: dict[str, Any]) -> Wharf:
    """ build wharf-object from parsed dict """

    PACKAGES: str = "packages"
    MANAGER: str = "manager"
    NAMES: str = "names"

    wharf: Wharf = Wharf()

    if not MANAGER in parsed[PACKAGES]:
        print("manager key missing in wharf file")
        return None
    wharf.manager = parsed[PACKAGES][MANAGER]

    if not NAMES in parsed[PACKAGES]:
        print("names key missing in wharf file")
        return None
    wharf.names = parsed[PACKAGES][NAMES]
    
    return wharf