from typing import Any
import parse

def main():
    # parse file and build wharf object
    parsed: dict[str, Any] = parse.parse_toml("wharf.toml")
    if parsed == None:
        exit(1)

    wharf: parse.Wharf = parse.build_wharf(parsed)

    # install packages
    success: bool = wharf.install()
    if success:
        print("installation successful.")
    else:
        exit(1)


if __name__ == "__main__":
    main()