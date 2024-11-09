from __future__ import annotations

import argparse
from enum import Enum

class MyArgs:
    class Mode(Enum):
        DEFAULT = 1,
        MONITOR = 2,
    mode: Mode

    _instance = None
    def __new__(cls) -> MyArgs:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        parser = argparse.ArgumentParser(description="!!! Currently, only the --monitor feature is implemented !!! This is a simple clipboard CLI application. Please see for detail: https://github.com/hatomania/clip")
        parser.add_argument("--monitor", help="Monitors what is added to the clipboard and outputs it to stdout.", default=False, action='store_true')
        args = parser.parse_args()

        self.mode = self.Mode.DEFAULT
        if bool(args.monitor) is True:
            self.mode = self.Mode.MONITOR

MyArgs() # create the singleton instance here
