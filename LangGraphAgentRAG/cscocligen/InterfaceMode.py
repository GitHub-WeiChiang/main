import cscocligen.IOSMode

class InterfaceMode(cscocligen.IOSMode.IOSMode):
    def __init__(self, interface_name, commands=None):
        super().__init__(commands)

        if commands is not None:
            return

        self._append_command("conf t\n")
        self._append_command("int " + interface_name + "\n")

    def no_shut(self):
        self._append_command("no shut\n")
        return self

    def shut(self):
        self._append_command("shut\n")
        return self

    def description(self, annotation: str):
        self._append_command("description " + annotation + "\n")
        return self
