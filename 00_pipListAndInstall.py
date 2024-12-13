#!/usr/bin/env python3

# https://docs.python.org/3/library/logging.config.html

import subprocess

if __name__ == "__main__":
    # subprocess.run(["ls", "-l"])
    pkgs = [line.strip() for line in open(".pip.list", "r")]
    """
    # output of pip list in .pip.list
    # the output first 2 lines has the header info
    # list slicing is forgiving with out of bounds, so 
    # directly start with the 2 element
    """
    for package in pkgs[2:]:
        pkg = package.split()[0]
        print(pkg)
        subprocess.run(["pip3", "install", pkg])
