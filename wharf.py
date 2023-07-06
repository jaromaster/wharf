import subprocess

# supported managers
MAN_PACMAN: str = "pacman"
MAN_APT: str = "apt"

# name of wharf file
WHARF_PATH: str = "wharf.toml"

class Wharf():
    """ class to model wharf-file contents """
    manager: str = ""
    names: list[str] = []

    def __str__(self) -> str:
        return f"Wharf[manager=\"{self.manager}\", names={self.names}]"
    
    def install(self) -> bool:
        """ install packages using manager """

        command: list[str] = []
        if self.manager == MAN_PACMAN:
            command = ["pacman", "-Sy", "--noconfirm"]
            command.extend(self.names)

        elif self.manager == MAN_APT: # TODO testing
            command = ["apt", "install", "-y"]
            command.extend(self.names)

        else:
            print(f"package manager '{self.manager}' not supported")
            return False

        try:
            res = subprocess.run(command)
            if res.returncode == 0:
                return False
        except Exception:
            print(f"Make sure {self.manager} is installed and you are running Wharf as root.")
            return False
            

        return True