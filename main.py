#!/usr/bin/env python3
from typing import Any
import sys
import parse
import wharf
import usage
import generate


def main():
    # check for args
    if len(sys.argv) == 2:
        operation: str = sys.argv[1]

        if operation == "-h" or operation == "help":
            usage.print_usage()
            exit(0)
        elif operation == "-n" or operation == "new":
            generate.new_wharf_toml()
            print("generated new wharf file")
            exit(0)
        else:
            print(f"invalid argument '{operation}'")
            exit(1)


    # parse file and build wharf object
    parsed: dict[str, Any] = parse.parse_toml(wharf.WHARF_PATH)
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