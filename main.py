#!/usr/bin/env python3
from typing import Any
import parse
import wharf


def main():
    # parse file and build wharf object
    WHARF_PATH: str = "wharf.toml"
    parsed: dict[str, Any] = parse.parse_toml(WHARF_PATH)
    if parsed == None:
        exit(1)

    w: wharf.Wharf = parse.build_wharf(parsed)

    # install packages
    success: bool = w.install()
    if success:
        print("installation successful.")
    else:
        exit(1)


if __name__ == "__main__":
    main()