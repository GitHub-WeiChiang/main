"""
Command Pattern.
"""

# Abstract base classes.
from abc import ABCMeta, abstractmethod
# IOSCommandBuilder module.
from CommandBuilder.IOSMode import IOSMode
from CommandBuilder.ManagerMode import ManagerMode
from CommandBuilder.ConfigMode import ConfigMode
from CommandBuilder.InterfaceMode import InterfaceMode
from CommandBuilder.RIPMode import RIPMode
from CommandBuilder.EIGRPMode import EIGRPMode
from CommandBuilder.OSPFMode import OSPFMode
# Config class.
from Config import Config
# Police name prefix.
# self.POLICE_NAME_PREFIX: str = "QoS_"
# Interval time of remote control command send.
# self.REMOTE_CTRL_COMMAND_INTERVAL_LONG_TIME: float = 5


class Command(metaclass=ABCMeta):
    """
    Command Interface.
    """

    def __init__(self, connect_info: tuple, command_info: list):
        """
        :param connect_info:
            Format refer to the following description, tuple = (ip, port, username, password).
        :param command_info:
            Customized for each command class.
        """

        # Required parameters.
        self.connect_info: tuple = connect_info
        self.command_info: list = command_info

    @abstractmethod
    def execute(self) -> (bool, list, str):
        """
        Remote control command execute function.

        :return:
            Return the result of remote command execution with tuple type (is_success, recv_list, msg).
        """
        pass

    @abstractmethod
    def undo(self) -> (bool, list, str):
        """
        Remote control command undo function.

        :return:
            Return the result of remote command execution with tuple type (is_success, recv_list, msg).
        """
        pass

# ============================================================
# --------------------------- Open ---------------------------
# ============================================================


class OpenPort(Command):
    def execute(self) -> (bool, list, str):
        # command_info[0] -> Interface Name.
        return InterfaceMode(self.command_info[0]).no_shut().exec(self.connect_info)

    def undo(self) -> (bool, list, str):
        # command_info[0] -> Interface Name.
        return InterfaceMode(self.command_info[0]).shut().exec(self.connect_info)


class OpenPortSecurity(Command):
    def execute(self) -> (bool, list, str):
        # command_info[0] -> Interface Name.
        return InterfaceMode(self.command_info[0]).port_security().exec(self.connect_info)

    def undo(self) -> (bool, list, str):
        # command_info[0] -> Interface Name.
        return InterfaceMode(self.command_info[0]).no_port_security().exec(self.connect_info)


class OpenPortSecuritySticky(Command):
    def execute(self) -> (bool, list, str):
        # command_info[0] -> Interface Name.
        return InterfaceMode(self.command_info[0]).port_security_sticky().exec(self.connect_info)

    def undo(self) -> (bool, list, str):
        # command_info[0] -> Interface Name.
        return InterfaceMode(self.command_info[0]).no_port_security_sticky().exec(self.connect_info)


class OpenPortSecurityStatic(Command):
    def execute(self) -> (bool, list, str):
        # command_info[0] -> Interface Name.
        # command_info[1] -> MAC Address.
        return InterfaceMode(self.command_info[0]).port_security_static(self.command_info[1]).exec(self.connect_info)

    def undo(self) -> (bool, list, str):
        # command_info[0] -> Interface Name.
        # command_info[1] -> MAC Address.
        return InterfaceMode(self.command_info[0]).no_port_security_static(self.command_info[1]).exec(self.connect_info)


class OpenSnmpServer(Command):
    def execute(self) -> (bool, list, str):
        """
        This method will execute two steps.

        step 1: Bind to ems.
        step 2: Automatically enabled traps port security.
        """

        # command_info[0] -> EMS IP.
        return (
            ConfigMode()
            .snmp_server_bind(self.command_info[0])
            .snmp_server_enable_traps_port_security()
            .exec(self.connect_info)
        )

    def undo(self) -> (bool, list, str):
        """
        This is different from the execute() method,
        it cannot automatically disable traps port security,
        because there may be other applications that depend on it.
        """

        # command_info[0] -> EMS IP.
        return ConfigMode().no_snmp_server_bind(self.command_info[0]).exec(self.connect_info)

# ============================================================
# -------------------------- Close ---------------------------
# ============================================================


class ClosePort(Command):
    def execute(self) -> (bool, list, str):
        # command_info[0] -> Interface Name.
        return InterfaceMode(self.command_info[0]).shut().exec(self.connect_info)

    def undo(self) -> (bool, list, str):
        # command_info[0] -> Interface Name.
        return InterfaceMode(self.command_info[0]).no_shut().exec(self.connect_info)


class ClosePortSecurity(Command):
    def execute(self) -> (bool, list, str):
        # command_info[0] -> Interface Name.
        return InterfaceMode(self.command_info[0]).no_port_security().exec(self.connect_info)

    def undo(self) -> (bool, list, str):
        # command_info[0] -> Interface Name.
        return InterfaceMode(self.command_info[0]).port_security().exec(self.connect_info)


class ClosePortSecuritySticky(Command):
    def execute(self) -> (bool, list, str):
        # command_info[0] -> Interface Name.
        return InterfaceMode(self.command_info[0]).no_port_security_sticky().exec(self.connect_info)

    def undo(self) -> (bool, list, str):
        # command_info[0] -> Interface Name.
        return InterfaceMode(self.command_info[0]).port_security_sticky().exec(self.connect_info)


class ClosePortSecurityStatic(Command):
    def execute(self) -> (bool, list, str):
        # command_info[0] -> Interface Name.
        # command_info[1] -> MAC Address.
        return InterfaceMode(self.command_info[0]).no_port_security_static(self.command_info[1]).exec(self.connect_info)

    def undo(self) -> (bool, list, str):
        # command_info[0] -> Interface Name.
        # command_info[1] -> MAC Address.
        return InterfaceMode(self.command_info[0]).port_security_static(self.command_info[1]).exec(self.connect_info)


class CloseSnmpServer(Command):
    def execute(self) -> (bool, list, str):
        """
        This is different from the undo() method,
        it cannot automatically disable traps port security,
        because there may be other applications that depend on it.
        """

        # command_info[0] -> EMS IP.
        return ConfigMode().no_snmp_server_bind(self.command_info[0]).exec(self.connect_info)

    def undo(self) -> (bool, list, str):
        """
        This method will execute two steps.

        step 1: Bind to ems.
        step 2: Automatically enabled traps port security.
        """

        # command_info[0] -> EMS IP.
        return (
            ConfigMode()
            .snmp_server_bind(self.command_info[0])
            .snmp_server_enable_traps_port_security()
            .exec(self.connect_info)
        )

# ============================================================
# -------------------------- Create --------------------------
# ============================================================

# Note: The name of the part needs to be prefixed with the specified string to recognize.


class CreateVlan(Command):
    def execute(self) -> (bool, list, str):
        # command_info[0] -> Vlan Name.
        return ConfigMode().vlan(self.command_info[0]).exec(self.connect_info)

    def undo(self) -> (bool, list, str):
        raise NotImplementedError("This feature is not implemented.")


class CreatePolice(Command):
    def __init__(self, connect_info: tuple, command_info: list):
        # Add command name prefix.
        command_info[0] = Config().POLICE_NAME_PREFIX + command_info[0]

        # Super class call.
        super().__init__(connect_info, command_info)

    def execute(self) -> (bool, list, str):
        """
        This method will execute three steps.

        step 1: Create acl by name.
        step 2: Bind acl to class.
        step 3: Bind class to policy.
        """

        # command_info[0] -> Police Name. (Set acl, class, policy names to be the same.)
        # command_info[1] -> Src IP.
        # command_info[2] -> Dest IP.
        # command_info[3] -> cir.
        # command_info[4] -> bc.

        return (
            ConfigMode()
            .ext_nacl_permit(self.command_info[0], self.command_info[1], self.command_info[2])
            .cmap_bind(self.command_info[0], self.command_info[0])
            .pmap_bind(self.command_info[0], self.command_info[0], self.command_info[3], self.command_info[4])
            .exec(self.connect_info)
        )

    def undo(self) -> (bool, list, str):
        """
        This method will execute three steps.

        step 1: Unbind class to policy.
        step 2: Unbind acl to class.
        step 3: Destroy acl by name.
        """

        # command_info[0] -> Police Name. (The acl, class, policy names is be the same.)

        return (
            ConfigMode()
            .no_pmap_bind(self.command_info[0])
            .no_cmap_bind(self.command_info[0])
            .no_ext_nacl_permit(self.command_info[0])
            .exec(self.connect_info)
        )


class CreateAclPermit(Command):
    def execute(self) -> (bool, list, str):
        # command_info[0] -> Acl num.
        # command_info[1] -> Src IP.
        return ConfigMode().acl_permit(self.command_info[0], self.command_info[1]).exec(self.connect_info)

    def undo(self) -> (bool, list, str):
        raise NotImplementedError("This feature is not implemented.")


class CreateAclDeny(Command):
    def execute(self) -> (bool, list, str):
        # command_info[0] -> Acl num.
        # command_info[1] -> Src IP.
        return ConfigMode().acl_deny(self.command_info[0], self.command_info[1]).exec(self.connect_info)

    def undo(self) -> (bool, list, str):
        raise NotImplementedError("This feature is not implemented.")


class CreateExtAclPermit(Command):
    def execute(self) -> (bool, list, str):
        # command_info[0] -> Acl num.
        # command_info[1] -> Src IP.
        # command_info[2] -> Dest IP.
        return ConfigMode().ext_acl_permit(
            self.command_info[0], self.command_info[1], self.command_info[2]
        ).exec(self.connect_info)

    def undo(self) -> (bool, list, str):
        raise NotImplementedError("This feature is not implemented.")


class CreateExtAclDeny(Command):
    def execute(self) -> (bool, list, str):
        # command_info[0] -> Acl num.
        # command_info[1] -> Src IP.
        # command_info[2] -> Dest IP.
        return ConfigMode().ext_acl_deny(
            self.command_info[0], self.command_info[1], self.command_info[2]
        ).exec(self.connect_info)

    def undo(self) -> (bool, list, str):
        raise NotImplementedError("This feature is not implemented.")

# ============================================================
# --------------------------- Set ----------------------------
# ============================================================


class SetSpeed(Command):
    def execute(self) -> (bool, list, str):
        # command_info[0] -> Interface Name.
        # command_info[1] -> Speed.
        return InterfaceMode(self.command_info[0]).speed(self.command_info[1]).exec(self.connect_info)

    def undo(self) -> (bool, list, str):
        raise NotImplementedError("This feature is not implemented.")


class SetDuplex(Command):
    def execute(self) -> (bool, list, str):
        # command_info[0] -> Interface Name.
        # command_info[1] -> Duplex.
        return InterfaceMode(self.command_info[0]).duplex(self.command_info[1]).exec(self.connect_info)

    def undo(self) -> (bool, list, str):
        raise NotImplementedError("This feature is not implemented.")


class SetVlan(Command):
    def execute(self) -> (bool, list, str):
        # command_info[0] -> Interface Name.
        # command_info[1] -> Vlan Name.
        return InterfaceMode(self.command_info[0]).vlan(self.command_info[1]).exec(self.connect_info)

    def undo(self) -> (bool, list, str):
        raise NotImplementedError("This feature is not implemented.")


class SetPoliceIn(Command):
    def __init__(self, connect_info: tuple, command_info: list):
        # Add command name prefix.
        command_info[1] = Config().POLICE_NAME_PREFIX + command_info[1]

        # Super class call.
        super().__init__(connect_info, command_info)

    def execute(self) -> (bool, list, str):
        # command_info[0] -> Interface Name.
        # command_info[1] -> Police Name.
        return InterfaceMode(self.command_info[0]).policy_in(self.command_info[1]).exec(self.connect_info)

    def undo(self) -> (bool, list, str):
        # command_info[0] -> Interface Name.
        # command_info[1] -> Police Name.
        return InterfaceMode(self.command_info[0]).no_policy_in(self.command_info[1]).exec(self.connect_info)


class SetPoliceOut(Command):
    def __init__(self, connect_info: tuple, command_info: list):
        # Add command name prefix.
        command_info[1] = Config().POLICE_NAME_PREFIX + command_info[1]

        # Super class call.
        super().__init__(connect_info, command_info)

    def execute(self) -> (bool, list, str):
        # command_info[0] -> Interface Name.
        # command_info[1] -> Police Name.
        return InterfaceMode(self.command_info[0]).policy_out(self.command_info[1]).exec(self.connect_info)

    def undo(self) -> (bool, list, str):
        # command_info[0] -> Interface Name.
        # command_info[1] -> Police Name.
        return InterfaceMode(self.command_info[0]).no_policy_out(self.command_info[1]).exec(self.connect_info)


class SetAclIn(Command):
    def execute(self) -> (bool, list, str):
        # command_info[0] -> Interface Name.
        # command_info[1] -> Acl num.
        return InterfaceMode(self.command_info[0]).acl_in(self.command_info[1]).exec(self.connect_info)

    def undo(self) -> (bool, list, str):
        raise NotImplementedError("This feature is not implemented.")


class SetAclOut(Command):
    def execute(self) -> (bool, list, str):
        # command_info[0] -> Interface Name.
        # command_info[1] -> Acl num.
        return InterfaceMode(self.command_info[0]).acl_out(self.command_info[1]).exec(self.connect_info)

    def undo(self) -> (bool, list, str):
        raise NotImplementedError("This feature is not implemented.")


class SetPortSecurityMaximum(Command):
    def execute(self) -> (bool, list, str):
        # command_info[0] -> Interface Name.
        # command_info[1] -> Port security maximum num.
        return InterfaceMode(self.command_info[0]).port_security_max(self.command_info[1]).exec(self.connect_info)

    def undo(self) -> (bool, list, str):
        raise NotImplementedError("This feature is not implemented.")


class SetPortSecurityVioProtect(Command):
    def execute(self) -> (bool, list, str):
        # command_info[0] -> Interface Name.
        return InterfaceMode(self.command_info[0]).port_security_vio_protect().exec(self.connect_info)

    def undo(self) -> (bool, list, str):
        raise NotImplementedError("This feature is not implemented.")


class SetPortSecurityVioRestrict(Command):
    def execute(self) -> (bool, list, str):
        # command_info[0] -> Interface Name.
        return InterfaceMode(self.command_info[0]).port_security_vio_restrict().exec(self.connect_info)

    def undo(self) -> (bool, list, str):
        raise NotImplementedError("This feature is not implemented.")


class SetPortSecurityVioShutdown(Command):
    def execute(self) -> (bool, list, str):
        # command_info[0] -> Interface Name.
        return InterfaceMode(self.command_info[0]).port_security_vio_shutdown().exec(self.connect_info)

    def undo(self) -> (bool, list, str):
        raise NotImplementedError("This feature is not implemented.")


class SetInterfaceDescription(Command):
    def execute(self) -> (bool, list, str):
        # command_info[0] -> Interface Name.
        # command_info[1] -> Interface Description (Alias).
        return InterfaceMode(self.command_info[0]).description(self.command_info[1]).exec(self.connect_info)

    def undo(self) -> (bool, list, str):
        raise NotImplementedError("This feature is not implemented.")

# ============================================================
# -------------------------- Unset ---------------------------
# ============================================================


class UnsetPoliceIn(Command):
    def __init__(self, connect_info: tuple, command_info: list):
        # Add command name prefix.
        command_info[1] = Config().POLICE_NAME_PREFIX + command_info[1]

        # Super class call.
        super().__init__(connect_info, command_info)

    def execute(self) -> (bool, list, str):
        # command_info[0] -> Interface Name.
        # command_info[1] -> Police Name.
        return InterfaceMode(self.command_info[0]).no_policy_in(self.command_info[1]).exec(self.connect_info)

    def undo(self) -> (bool, list, str):
        # command_info[0] -> Interface Name.
        # command_info[1] -> Police Name.
        return InterfaceMode(self.command_info[0]).policy_in(self.command_info[1]).exec(self.connect_info)


class UnsetPoliceOut(Command):
    def __init__(self, connect_info: tuple, command_info: list):
        # Add command name prefix.
        command_info[1] = Config().POLICE_NAME_PREFIX + command_info[1]

        # Super class call.
        super().__init__(connect_info, command_info)

    def execute(self) -> (bool, list, str):
        # command_info[0] -> Interface Name.
        # command_info[1] -> Police Name.
        return InterfaceMode(self.command_info[0]).no_policy_out(self.command_info[1]).exec(self.connect_info)

    def undo(self) -> (bool, list, str):
        # command_info[0] -> Interface Name.
        # command_info[1] -> Police Name.
        return InterfaceMode(self.command_info[0]).policy_out(self.command_info[1]).exec(self.connect_info)

# ============================================================
# -------------------------- Clear ---------------------------
# ============================================================


class ClearPortSecurityAll(Command):
    def execute(self) -> (bool, list, str):
        return ManagerMode().clear_port_security_all().exec(self.connect_info)

    def undo(self) -> (bool, list, str):
        raise NotImplementedError("This feature is not implemented.")


class ClearPolice(Command):
    def __init__(self, connect_info: tuple, command_info: list):
        # Add command name prefix.
        command_info[0] = Config().POLICE_NAME_PREFIX + command_info[0]

        # Super class call.
        super().__init__(connect_info, command_info)

    def execute(self) -> (bool, list, str):
        """
        This method will execute three steps.

        step 1: Unbind class to policy.
        step 2: Unbind acl to class.
        step 3: Destroy acl by name.
        """

        # command_info[0] -> Police Name. (The acl, class, policy names is be the same.)

        return (
            ConfigMode()
            .no_pmap_bind(self.command_info[0])
            .no_cmap_bind(self.command_info[0])
            .no_ext_nacl_permit(self.command_info[0])
            .exec(self.connect_info)
        )

    def undo(self) -> (bool, list, str):
        raise NotImplementedError("This feature is not implemented.")


# ============================================================
# --------------------------- Show ---------------------------
# ============================================================


class ShowPmapList(Command):
    def execute(self) -> (bool, list, str):
        return ManagerMode().sh_pmap().exec(self.connect_info)

    def undo(self) -> (bool, list, str):
        raise NotImplementedError("This feature is not implemented.")


class ShowPmapIntList(Command):
    def execute(self) -> (bool, list, str):
        return ManagerMode().sh_pmap_int().exec(self.connect_info)

    def undo(self) -> (bool, list, str):
        raise NotImplementedError("This feature is not implemented.")


class ShowRunningConfig(Command):
    def execute(self) -> (bool, list, str):
        return ManagerMode().sh_run().exec(self.connect_info, wait_time=Config().REMOTE_CTRL_COMMAND_INTERVAL_LONG_TIME)

    def undo(self) -> (bool, list, str):
        raise NotImplementedError("This feature is not implemented.")


class ShowPortSecurityAddress(Command):
    def execute(self) -> (bool, list, str):
        return ManagerMode().sh_port_security_address().exec(self.connect_info)

    def undo(self) -> (bool, list, str):
        raise NotImplementedError("This feature is not implemented.")


class ShowSnmpHost(Command):
    def execute(self) -> (bool, list, str):
        return ManagerMode().sh_snmp_host().exec(self.connect_info)

    def undo(self) -> (bool, list, str):
        raise NotImplementedError("This feature is not implemented.")

# ============================================================
# -------------------------- Other ---------------------------
# ============================================================


class Custom(Command):
    def execute(self) -> (bool, list, str):
        # !!!!! This is a dangerous operation !!!!!
        return IOSMode(self.command_info).exec(self.connect_info)

    def undo(self) -> (bool, list, str):
        raise NotImplementedError("This feature is not implemented.")


# Command Builder Operation Demonstration.
if __name__ == '__main__':
    # ----------------------------------------------------------------------------------------------------

    # Sample connect info.
    sample_connect_info: tuple = ('173.0.1.188', 22, 'admin', '!QAZ2wsx')

    # ----------------------------------------------------------------------------------------------------

    # Optional terminal operation.

    # InterfaceMode("gi1/0/4").shut().build()
    # InterfaceMode("gi1/0/4").shut().exec(sample_connect_info)

    # ----------------------------------------------------------------------------------------------------

    # Mode switch.
    print(ManagerMode().to_config().to_interface("gi1/0/4").build())
    # print(ManagerMode().to_config().to_manager().to_config().to_manager().to_config().to_manager().....)

    print()

    # ----------------------------------------------------------------------------------------------------

    # Macro operation.
    command_list: list = (ConfigMode()    # New "ConfigMode" Object and enter to config mode, return "Config".
                          .vlan("48763")    # Create vlan "48763", return "Config".
                          .to_interface("gi1/0/4")    # Enter interface "gi1/0/4", return "Interface".
                          .no_shut()    # Start up interface, return "Interface".
                          .vlan("48763")    # Assigned to vlan "48763", return "Interface".
                          .to_config()    # Back to config mode, return "Config".
                          .default_gateway("x.x.x.x")    # Set default gateway, return "Config".
                          .to_interface("gi1/0/5")    # Enter interface "gi1/0/5", return "Interface".
                          .no_shut()    # Start up interface, return "Interface".
                          .vlan("48763")    # Assigned to vlan "48763", return "Interface".
                          .to_interface("gi1/0/6")    # Enter interface "gi1/0/6", return "Interface".
                          .no_shut()    # Start up interface, return "Interface".
                          .vlan("48763")    # Assigned to vlan "48763", return "Interface".
                          .to_config()    # Back to config mode, return "Config".
                          .build())    # Call terminal operation to build command str list.

    for i in command_list:
        print(i, end="")

    print()

    # ----------------------------------------------------------------------------------------------------

    # Mode switch (jumping).
    # Following two programs are equivalent, the second one has better performance and less memory usage.
    print(ManagerMode().to_config().to_interface("gi1/0/4").to_config().to_manager().build())
    print(ManagerMode().to_interface("gi1/0/4").to_manager().build())

    print()

    # ----------------------------------------------------------------------------------------------------

    # Command isolation.
    # ManagerMode().to_config().to_interface()
    # ManagerMode().reload().exec(sample_connect_info)

    # ----------------------------------------------------------------------------------------------------

    # ACL.
    print(ConfigMode().acl_permit("1", "x.x.x.x").build())
    print(ConfigMode().acl_deny("2", "x.x.x.x").build())

    print(ConfigMode().ext_acl_permit("3", "x.x.x.x", "x.x.x.x").build())
    print(ConfigMode().ext_acl_permit("4", "x.x.x.x", "").build())
    print(ConfigMode().ext_acl_permit("5", "", "x.x.x.x").build())

    print(ConfigMode().ext_acl_deny("6", "x.x.x.x", "x.x.x.x").to_interface("gi1/0/4").acl_in("6").build())

    print()

    # ----------------------------------------------------------------------------------------------------

    # QoS.
    command_list: list = (
        ConfigMode()
        .ext_nacl_permit("ACL_5M", "any", "any")
        .cmap_bind("CLASS_5M", "ACL_5M")
        .pmap_bind("POLICY_5M", "CLASS_5M", "5000000", "100000")
        .to_interface("gi1/0/4")
        .policy_out("POLICY_5M")
        .build()
    )

    for i in command_list:
        print(i, end="")

    print()

    # print(
    #     ConfigMode()
    #     .ext_nacl_permit("ACL_5M", "any", "any")
    #     .cmap_bind("CLASS_5M", "ACL_5M")
    #     .pmap_bind("POLICY_5M", "CLASS_5M", "5000000", "100000")
    #     .to_interface("gi1/0/4")
    #     .policy_out("POLICY_5M")
    #     .exec(sample_connect_info)
    # )

    # ----------------------------------------------------------------------------------------------------

    # print(ShowPmapList().execute(sample_connect_info, []))

    # ----------------------------------------------------------------------------------------------------

    print(
        EIGRPMode("10")
        .to_rip()
        .to_interface("gi1/0/4")
        .to_config()
        .to_manager()
        .to_rip()
        .to_eigrp("10")
        .build()
    )

    print(RIPMode().to_eigrp("10").to_eigrp("20").variance("2").build())

    print(OSPFMode("10").to_eigrp("10").to_rip().to_ospf("20").to_ospf("10").build())
