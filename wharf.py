from typing import Any
import parse

def main():
    print("wharf")


if __name__ == "__main__":
    main()

    # parse file and build wharf object
    parsed: dict[str, Any] = parse.parse_toml("wharf.toml")
    wharf: parse.Wharf = parse.build_wharf(parsed)

    print(wharf)