# Avoid circular dependency caused by circular imports.
import CommandBuilder.IOSMode
import CommandBuilder.ManagerMode
import CommandBuilder.ConfigMode
import CommandBuilder.InterfaceMode
import CommandBuilder.RIPMode
import CommandBuilder.EIGRPMode


class OSPFMode(CommandBuilder.IOSMode.IOSMode):
    def __init__(self, process_id: str, commands: list = None):
        super().__init__(commands)

        # Increase flexibility and provide mode switching.
        if commands is not None:
            return

        # If this object is the source of the streams,
        # "OSPF" mode needs to be entered automatically.
        self._append_command("conf t\n")
        self._append_command("router ospf " + process_id + "\n")

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
        return CommandBuilder.EIGRPMode.EIGRPMode(as_num, self.build())

    def to_ospf(self, process_id: str):
        self._append_command("exit\n")
        self._append_command("router ospf " + process_id + "\n")
        return self

    # ============================================================
    # --------------------- Other Operations ---------------------
    # ============================================================

    def network_wildcard_mask(self, ip: str, wildcard_mask: str, area_id: str):
        self._append_command("network " + ip + " " + wildcard_mask + " area " + area_id + "\n")
        return self

    def router_id(self, router_id: str):
        self._append_command("router-id " + router_id + "\n")
        return self

    def reset(self):
        # Disabled, just to be on the safe side.
        # self._append_command("do clear ip ospf process\n")
        # self._append_command("y\n")
        return self

    def default_info_orig(self):
        self._append_command("default-information originate\n")
        return self

    def router_comp(self, area_id: str, ip: str, mask: str):
        self._append_command("area " + area_id + " range " + ip + " " + mask + "\n")
        return self
