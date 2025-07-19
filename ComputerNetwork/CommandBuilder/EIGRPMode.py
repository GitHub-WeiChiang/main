# Avoid circular dependency caused by circular imports.
import CommandBuilder.IOSMode
import CommandBuilder.ManagerMode
import CommandBuilder.ConfigMode
import CommandBuilder.InterfaceMode
import CommandBuilder.RIPMode
import CommandBuilder.OSPFMode


class EIGRPMode(CommandBuilder.IOSMode.IOSMode):
    def __init__(self, as_num: str, commands: list = None):
        super().__init__(commands)

        # Increase flexibility and provide mode switching.
        if commands is not None:
            return

        # If this object is the source of the streams,
        # "EIGRP" mode needs to be entered automatically.
        self._append_command("conf t\n")
        self._append_command("router eigrp " + as_num + "\n")

    # ============================================================
    # ----------------------- Mode Switch ------------------------
    # ============================================================

    # ---------------------------- Up ----------------------------

    def to_manager(self):
        self._append_command("exit\n")
        self._append_command("exit\n")
        return CommandBuilder.ManagerMode.ManagerMode(self.build())

    def to_config(self):
        self._append_command("exit\n")
        return CommandBuilder.ConfigMode.ConfigMode(self.build())

    # ------------------------- Parallel -------------------------

    def to_interface(self, interface_name: str):
        self._append_command("int " + interface_name + "\n")
        return CommandBuilder.InterfaceMode.InterfaceMode(interface_name, self.build())

    def to_loopback(self, interface_num: str):
        interface_name: str = "loopback " + interface_num
        return self.to_interface(interface_name)

    def to_rip(self):
        self._append_command("exit\n")
        self._append_command("router rip\n")
        return CommandBuilder.RIPMode.RIPMode(self.build())

    def to_eigrp(self, as_num: str):
        self._append_command("exit\n")
        self._append_command("router eigrp " + as_num + "\n")
        return self

    def to_ospf(self, process_id: str):
        self._append_command("exit\n")
        self._append_command("router ospf " + process_id + "\n")
        return CommandBuilder.OSPFMode.OSPFMode(process_id, self.build())

    # ============================================================
    # --------------------- Other Operations ---------------------
    # ============================================================

    def network(self, ip: str):
        self._append_command("network " + ip + "\n")
        return self

    def network_wildcard_mask(self, ip: str, wildcard_mask: str):
        self._append_command("network " + ip + " " + wildcard_mask + "\n")
        return self

    def network_all(self):
        self._append_command("network 0.0.0.0\n")
        return self

    def no_auto_summary(self):
        self._append_command("no auto-summary\n")
        return self

    def distance(self, internal_dist: str, external_dist: str):
        self._append_command("distance eigrp " + internal_dist + " " + external_dist + "\n")
        return self

    def variance(self, param: str):
        self._append_command("variance " + param + "\n")
        return self
