# WHARF

### simple tool for porting linux packages from one PC to another

## Features
- wharf file for specifying packages and package manager
- install all specified packages on different systems
- supported managers: pacman, apt

## How it works
- `./main.py -n`
- open new `wharf.toml` and specify manager and packages to port
- distribute `wharf.toml`
- `sudo ./main.py` to install all packages on new system