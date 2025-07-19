# Avoid circular dependency caused by circular imports.
import CommandBuilder.IOSMode
import CommandBuilder.ManagerMode
import CommandBuilder.ConfigMode
import CommandBuilder.RIPMode
import CommandBuilder.EIGRPMode
import CommandBuilder.OSPFMode


class InterfaceMode(CommandBuilder.IOSMode.IOSMode):
    def __init__(self, interface_name: str, commands: list = None):
        super().__init__(commands)

        # Increase flexibility and provide mode switching.
        if commands is not None:
            return

        # If this object is the source of the streams,
        # "Interface" mode needs to be entered automatically.
        self._append_command("conf t\n")
        self._append_command("int " + interface_name + "\n")

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
        return self

    def to_loopback(self, interface_num: str):
        interface_name: str = "loopback " + interface_num
        return self.to_interface(interface_name)

    def to_rip(self):
        self._append_command("router rip\n")
        return CommandBuilder.RIPMode.RIPMode(self.build())

    def to_eigrp(self, as_num: str):
        self._append_command("router eigrp " + as_num + "\n")
        return CommandBuilder.EIGRPMode.EIGRPMode(as_num, self.build())

    def to_ospf(self, process_id: str):
        self._append_command("router ospf " + process_id + "\n")
        return CommandBuilder.OSPFMode.OSPFMode(process_id, self.build())

    # ============================================================
    # --------------------- Other Operations ---------------------
    # ============================================================

    def no_shut(self):
        self._append_command("no shut\n")
        return self

    def shut(self):
        self._append_command("shut\n")
        return self

    def speed(self, speed: str):
        self._append_command("speed " + speed + "\n")
        return self

    def duplex(self, duplex: str):
        self._append_command("duplex " + duplex + "\n")
        return self

    def vlan(self, vlan_name: str):
        self._append_command("switchport access vlan " + vlan_name + "\n")
        return self

    def trunk(self):
        self._append_command("switchport mode trunk\n")
        return self

    def access(self):
        self._append_command("switchport mode access\n")
        return self

    def no_port_security(self):
        self._append_command("no switchport port-security\n")
        return self

    def port_security(self):
        self._append_command("switchport port-security\n")
        return self

    def port_security_max(self, num: str):
        self._append_command("switchport port-security maximum " + num + "\n")
        return self

    def port_security_static(self, mac: str):
        self._append_command("switchport port-security mac-address " + mac + "\n")
        return self

    def no_port_security_static(self, mac: str):
        self._append_command("no switchport port-security mac-address " + mac + "\n")
        return self

    def port_security_sticky(self):
        self._append_command("switchport port-security mac-address sticky\n")
        return self

    def no_port_security_sticky(self):
        self._append_command("no switchport port-security mac-address sticky\n")
        return self

    def port_security_vio_protect(self):
        self._append_command("switchport port-security violation protect\n")
        return self

    def port_security_vio_restrict(self):
        self._append_command("switchport port-security violation restrict\n")
        return self

    def port_security_vio_shutdown(self):
        self._append_command("switchport port-security violation shutdown\n")
        return self

    def ip(self, ip: str, mask: str):
        self._append_command("ip address " + ip + " " + mask + "\n")
        return self

    def ip_summary_eigrp(self, as_num: str, ip: str, mask: str):
        self._append_command("ip summary-address eigrp " + as_num + " " + ip + " " + mask + "\n")
        return self

    def description(self, annotation: str):
        self._append_command("description " + annotation + "\n")
        return self

    def channel_group(self, num: str, mode: str):
        self._append_command("channel-group " + num + " mode " + mode + "\n")
        return self

    def acl_in(self, num: str):
        self._append_command("ip access-group " + num + " in\n")
        return self

    def acl_out(self, num: str):
        self._append_command("ip access-group " + num + " out\n")
        return self

    def policy_in(self, policy_name: str):
        self._append_command("service-policy input " + policy_name + "\n")
        return self

    def policy_out(self, policy_name: str):
        self._append_command("service-policy output " + policy_name + "\n")
        return self

    def no_policy_in(self, policy_name: str):
        self._append_command("no service-policy input " + policy_name + "\n")
        return self

    def no_policy_out(self, policy_name: str):
        self._append_command("no service-policy output " + policy_name + "\n")
        return self

    def ospf_dead_interval(self, sec: str):
        self._append_command("ip ospf dead-interval " + sec + "\n")
        return self

    def ospf_hello_interval(self, sec: str):
        self._append_command("ip ospf hello-interval " + sec + "\n")
        return self

    def ospf_cost(self, cost: str):
        self._append_command("ip ospf cost " + cost + "\n")
        return self

    def ospf_priority(self, priority: str):
        self._append_command("ip ospf priority " + priority + "\n")
        return self

    def bandwidth(self, bandwidth: str):
        self._append_command("bandwidth " + bandwidth + "\n")
        return self
