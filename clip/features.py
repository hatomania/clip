import pyperclip

from clip.myargs import MyArgs

class Feature:
    def do(self) -> int:
        return 0

class Default(Feature):
    def do(self) -> int:
        print("Currently, only the --monitor feature is implemented. see --help")
        return 0

class Monitor(Feature):
    def do(self) -> int:
        loop = True
        while loop:
            try:
                print(pyperclip.waitForNewPaste())
            except KeyboardInterrupt:
                loop = False
        return 0

class Factory:
    def create(self) -> Feature:
        ret = None
        if MyArgs().mode is MyArgs().Mode.MONITOR:
            ret = Monitor()
        else:
            ret = Default()
        return ret
