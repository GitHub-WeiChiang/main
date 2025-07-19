# Avoid circular dependency caused by circular imports.
import CommandBuilder.IOSMode
import CommandBuilder.ConfigMode
import CommandBuilder.InterfaceMode
import CommandBuilder.RIPMode
import CommandBuilder.EIGRPMode
import CommandBuilder.OSPFMode


class ManagerMode(CommandBuilder.IOSMode.IOSMode):
    # ============================================================
    # ----------------------- Mode Switch ------------------------
    # ============================================================

    # --------------------------- Down ---------------------------

    def to_config(self):
        self._append_command("conf t\n")
        return CommandBuilder.ConfigMode.ConfigMode(self.build())

    def to_interface(self, interface_name: str):
        self._append_command("conf t\n")
        self._append_command("int " + interface_name + "\n")
        return CommandBuilder.InterfaceMode.InterfaceMode(interface_name, self.build())

    def to_loopback(self, interface_num: str):
        interface_name: str = "loopback " + interface_num
        return self.to_interface(interface_name)

    def to_rip(self):
        self._append_command("conf t\n")
        self._append_command("router rip\n")
        return CommandBuilder.RIPMode.RIPMode(self.build())

    def to_eigrp(self, as_num: str):
        self._append_command("conf t\n")
        self._append_command("router eigrp " + as_num + "\n")
        return CommandBuilder.EIGRPMode.EIGRPMode(as_num, self.build())

    def to_ospf(self, process_id: str):
        self._append_command("conf t\n")
        self._append_command("router ospf " + process_id + "\n")
        return CommandBuilder.OSPFMode.OSPFMode(process_id, self.build())

    # ============================================================
    # --------------------- Other Operations ---------------------
    # ============================================================

    def sh_vlan(self):
        self._append_command("sh vlan\n")
        return self

    def sh_version(self):
        self._append_command("sh version\n")
        return self

    def sh_history(self):
        self._append_command("sh history\n")
        return self

    def sh_startup(self):
        self._append_command("sh startup\n")
        return self

    def sh_cdp(self):
        self._append_command("sh cdp neighbors\n")
        return self

    def sh_ip_route(self):
        self._append_command("sh ip route\n")
        return self

    def sh_ip_int(self):
        self._append_command("sh ip int br\n")
        return self

    def sh_ip_flow(self):
        self._append_command("sh ip cache flow\n")
        return self

    def sh_ip_traffic(self):
        self._append_command("sh ip traffic\n")
        return self

    def sh_etherchannel(self):
        self._append_command("show etherchannel summary\n")
        return self

    def sh_etherchannel_load_balance(self):
        self._append_command("show etherchannel load-balance\n")
        return self

    def sh_run(self):
        # 如果真的嫌太慢，可以考慮透過 Cisco PI 的 REST API 獲取 (但是要注意同步問題)，
        # 有兩隻 API 可以使用:
        # 1. GET Bulk export sanitized configuration archives
        # 2. GET Bulk export unsanitized configuration
        # sanitized 表示: 獲取到的資料經過編輯、處理、消毒，是安全的，已經過濾的敏感信息 (用戶名與密碼等)。
        # unsanitized 表示: 獲取到的資料非常的純。
        self._append_command("show run\n")
        return self

    def sh_acl(self):
        self._append_command("show access-lists\n")
        return self

    def sh_pmap(self):
        self._append_command("show policy-map\n")
        return self

    def sh_pmap_int(self):
        self._append_command("show policy-map int\n")
        return self

    def sh_cmap(self):
        self._append_command("show class-map\n")
        return self

    def sh_mac_address_table(self):
        self._append_command("show mac address-table\n")
        return self

    def sh_port_security(self):
        self._append_command("show port-security\n")
        return self

    def sh_port_security_address(self):
        self._append_command("show port-security address\n")
        return self

    def sh_port_security_int(self, interface_name: str):
        self._append_command("show port-security int " + interface_name + "\n")
        return self

    def sh_snmp_host(self):
        self._append_command("show snmp host\n")
        return self

    def sh_sserver_enable_traps(self):
        self._append_command("show running-config | include snmp-server enable traps\n")
        return self

    def clear_acl_count(self):
        self._append_command("clear access-list counters\n")
        return self

    def clear_mac_address_table(self):
        self._append_command("clear mac address-table\n")
        return self

    def clear_port_security_all(self):
        self._append_command("clear port-security all\n")
        return self

    def write(self):
        self._append_command("write\n")
        return self

    def reload(self):
        # Disabled, just to be on the safe side.
        # self._append_command("reload\n")
        return self


# ManagerMode Operation Demonstration.
if __name__ == '__main__':
    # Sample connect info.
    sample_connect_info: tuple = ('173.0.1.188', 22, 'admin', '!QAZ2wsx')

    print(ManagerMode().sh_pmap().exec(sample_connect_info))
