import wharf

def new_wharf_toml():
    """ generate a new wharf file template """

    content: str = """[packages] \
        \rmanager = "pacman or apt" \
        \rnames = [ \
            \r\t"package1", \
            \r\t"package2", \
        \r]"""

    new_wharf_file = open(wharf.WHARF_PATH, "w")
    new_wharf_file.write(content)
    new_wharf_file.close()