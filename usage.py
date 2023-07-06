

def print_usage():
    """ print help and usage """

    print("USAGE:")
    print("Install packages:")
    print("1. move to dir containing 'wharf.toml'")
    print("2. run 'sudo ./main.py' to install\n")

    print("Create new 'wharf.toml':")
    print("1. run 'sudo ./main.py new' or 'sudo ./main.py -n'")
    print("2. set manager")
    print("3. add packages to install\n")

    print("Package managers supported:")
    print("1. pacman")
    print("2. apt")