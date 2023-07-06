#!/usr/bin/env python3
from typing import Any
import sys
import parse
import wharf
import usage


def main():
    if len(sys.argv) == 2:
        operation: str = sys.argv[1]

        if operation == "-h" or operation == "help":
            usage.print_usage()
            exit(0)
        elif operation == "-n" or operation == "new":
            # TODO generate new "wharf.toml"
            print("generating new wharf.toml file")
            exit(0)
        else:
            print(f"invalid argument '{operation}'")
            exit(1)


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