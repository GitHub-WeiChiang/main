# Avoid circular dependency caused by circular imports.
import CommandBuilder.IOSMode
import CommandBuilder.ManagerMode
import CommandBuilder.InterfaceMode
import CommandBuilder.RIPMode
import CommandBuilder.EIGRPMode
import CommandBuilder.OSPFMode


class ConfigMode(CommandBuilder.IOSMode.IOSMode):
    def __init__(self, commands: list = None):
        super().__init__(commands)

        # Increase flexibility and provide mode switching.
        if commands is not None:
            return

        # If this object is the source of the streams,
        # "Config" mode needs to be entered automatically.
        self._append_command("conf t\n")

    # ============================================================
    # ----------------------- Mode Switch ------------------------
    # ============================================================

    # ---------------------------- Up ----------------------------

    def to_manager(self):
        self._append_command("exit\n")
        return CommandBuilder.ManagerMode.ManagerMode(self.build())

    # --------------------------- Down ---------------------------

    def to_interface(self, interface_name: str):
        self._append_command("int " + interface_name + "\n")
        return CommandBuilder.InterfaceMode.InterfaceMode(interface_name, self.build())

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

    def vlan(self, vlan_name: str):
        self._append_command("vlan " + vlan_name + "\n")
        self._append_command("exit\n")
        return self

    def no_vlan(self, vlan_name: str):
        self._append_command("no vlan " + vlan_name + "\n")
        return self

    def static_route(self, ip: str, mask: str, interface_name: str):
        self._append_command("ip route " + ip + " " + mask + " " + interface_name + "\n")
        return self

    def no_static_route(self, ip: str, mask: str, interface_name: str):
        self._append_command("no ip route " + ip + " " + mask + " " + interface_name + "\n")
        return self

    def next_hop(self, ip: str, mask: str, next_hop_ip: str):
        self._append_command("ip route " + ip + " " + mask + " " + next_hop_ip + "\n")
        return self

    def default_gateway(self, ip: str):
        self._append_command("ip default-gateway " + ip + "\n")
        return self

    def default_network(self, ip: str):
        self._append_command("ip default-network " + ip + "\n")
        return self

    def default_route(self, next_hop_ip: str):
        self._append_command("ip route 0.0.0.0 0.0.0.0 " + next_hop_ip + "\n")
        return self

    def routing(self):
        self._append_command("ip routing\n")
        return self

    def hostname(self, name: str):
        self._append_command("hostname " + name + "\n")
        return self

    def cdp(self):
        self._append_command("cdp run\n")
        return self

    def no_cdp(self):
        self._append_command("no cdp run\n")
        return self

    def port_channel_load_balance(self, state: str):
        self._append_command("port-channel load-balance " + state + "\n")
        return self

    def acl_permit(self, num: str, ip: str):
        self._append_command("access-list " + num + " permit host " + ip + "\n")
        return self

    def acl_deny(self, num: str, ip: str):
        self._append_command("access-list " + num + " deny host " + ip + "\n")
        return self

    def ext_acl_permit(self, num: str, src_ip: str, dest_ip: str):
        # Command formatting.
        src: str = src_ip if src_ip == "any" else "host " + src_ip
        dest: str = dest_ip if dest_ip == "any" else "host " + dest_ip

        self._append_command("access-list " + num + " permit ip " + src + " " + dest + "\n")
        return self

    def ext_acl_deny(self, num: str, src_ip: str, dest_ip: str):
        # Command formatting.
        src: str = src_ip if src_ip == "any" else "host " + src_ip
        dest: str = dest_ip if dest_ip == "any" else "host " + dest_ip

        self._append_command("access-list " + num + " deny ip " + src + " " + dest + "\n")
        return self

    def ext_nacl_permit(self, name: str, src_ip: str, dest_ip: str):
        # Command formatting.
        src: str = src_ip if src_ip == "any" else "host " + src_ip
        dest: str = dest_ip if dest_ip == "any" else "host " + dest_ip

        self._append_command("ip access-list extended " + name + "\n")
        self._append_command("permit ip " + src + " " + dest + "\n")
        self._append_command("exit\n")
        return self

    def no_ext_nacl_permit(self, name: str):
        self._append_command("no ip access-list extended " + name + "\n")
        return self

    def cmap_bind(self, class_name: str, acl_name: str):
        """
        Bind ACL to CLASS.
        """

        self._append_command("class-map match-all " + class_name + "\n")
        self._append_command("match access-group name " + acl_name + "\n")
        self._append_command("exit\n")
        return self

    def no_cmap_bind(self, name: str):
        self._append_command("no class-map " + name + "\n")
        return self

    def pmap_bind(self, policy_name: str, class_name: str, cir: str, bc: str):
        """
        Bind CLASS to POLICY.
        """

        self._append_command("policy-map " + policy_name + "\n")
        self._append_command("class " + class_name + "\n")
        self._append_command("police " + cir + " " + bc + "\n")
        self._append_command("exceed-action drop\n")
        self._append_command("exit\n")
        self._append_command("exit\n")
        self._append_command("exit\n")
        return self

    def no_pmap_bind(self, name: str):
        self._append_command("no policy-map " + name + "\n")
        return self

    def vtp_mode_s(self):
        """
        Set vtp to server mode.
        """

        self._append_command("vtp mode server\n")
        return self

    def vtp_mode_c(self):
        """
        Set vtp to client mode.
        """

        self._append_command("vtp mode client\n")
        return self

    def vtp_mode_t(self):
        """
        Set vtp to transparent mode.
        """

        self._append_command("vtp mode transparent\n")
        return self

    def vtp_domain(self, name: str):
        self._append_command("vtp domain " + name + "\n")
        return self

    def vtp_password(self, password: str):
        self._append_command("vtp password " + password + "\n")
        return self

    def no_loopback(self, interface_num: str):
        interface_name: str = "loopback " + interface_num

        self._append_command("no int " + interface_name + "\n")
        return self

    def snmp_server_bind(self, ip: str):
        self._append_command("snmp-server host " + ip + " version 2c public\n")
        return self

    def no_snmp_server_bind(self, ip: str):
        self._append_command("no snmp-server host " + ip + " version 2c public\n")
        return self

    def snmp_server_enable_traps_port_security(self):
        self._append_command("snmp-server enable traps port-security\n")
        return self

    def no_snmp_server_enable_traps_port_security(self):
        self._append_command("no snmp-server enable traps port-security\n")
        return self
