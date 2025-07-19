"""
Command Pattern.
"""

# Abstract base classes.
from abc import ABCMeta
# Import singleton decorator.
from Decorator import singleton
# Import tuple module of typing.
from typing import Dict, List
# Import default dict.
from collections import defaultdict
# Import commands.
from RemoteControl.CommandList import Command
# Open
from RemoteControl.CommandList import OpenPort
from RemoteControl.CommandList import OpenPortSecurity, OpenPortSecuritySticky, OpenPortSecurityStatic
from RemoteControl.CommandList import OpenSnmpServer
# Close
from RemoteControl.CommandList import ClosePort
from RemoteControl.CommandList import ClosePortSecurity, ClosePortSecuritySticky, ClosePortSecurityStatic
from RemoteControl.CommandList import CloseSnmpServer
# Create
from RemoteControl.CommandList import CreateVlan, CreatePolice
from RemoteControl.CommandList import CreateAclPermit, CreateAclDeny, CreateExtAclPermit, CreateExtAclDeny
# Set
from RemoteControl.CommandList import SetSpeed, SetDuplex, SetVlan
from RemoteControl.CommandList import SetPoliceIn, SetPoliceOut, SetAclIn, SetAclOut
from RemoteControl.CommandList import SetPortSecurityMaximum
from RemoteControl.CommandList import SetPortSecurityVioProtect
from RemoteControl.CommandList import SetPortSecurityVioRestrict
from RemoteControl.CommandList import SetPortSecurityVioShutdown
from RemoteControl.CommandList import SetInterfaceDescription
# Unset
from RemoteControl.CommandList import UnsetPoliceIn, UnsetPoliceOut
# Clear
from RemoteControl.CommandList import ClearPortSecurityAll
from RemoteControl.CommandList import ClearPolice
# Show
from RemoteControl.CommandList import ShowPmapList, ShowPmapIntList
from RemoteControl.CommandList import ShowRunningConfig
from RemoteControl.CommandList import ShowPortSecurityAddress
from RemoteControl.CommandList import ShowSnmpHost
# Other
from RemoteControl.CommandList import Custom
# Command enum.
from RemoteControl.CommandEnum import CommandEnum


@singleton
class RemoteController:
    """
    Remote Controller.
    """

    def __init__(self):
        self.__commands: Dict[CommandEnum, ABCMeta] = {
            # Open
            CommandEnum.OPEN_PORT: OpenPort,
            CommandEnum.OPEN_PORT_SECURITY: OpenPortSecurity,
            CommandEnum.OPEN_PORT_SECURITY_STICKY: OpenPortSecuritySticky,
            CommandEnum.OPEN_PORT_SECURITY_STATIC: OpenPortSecurityStatic,
            CommandEnum.OPEN_SNMP_SERVER: OpenSnmpServer,
            # Close
            CommandEnum.CLOSE_PORT: ClosePort,
            CommandEnum.CLOSE_PORT_SECURITY: ClosePortSecurity,
            CommandEnum.CLOSE_PORT_SECURITY_STICKY: ClosePortSecuritySticky,
            CommandEnum.CLOSE_PORT_SECURITY_STATIC: ClosePortSecurityStatic,
            CommandEnum.CLOSE_SNMP_SERVER: CloseSnmpServer,
            # Create
            CommandEnum.CREATE_VLAN: CreateVlan,
            CommandEnum.CREATE_POLICE: CreatePolice,
            CommandEnum.CREATE_ACL_PERMIT: CreateAclPermit,
            CommandEnum.CREATE_ACL_DENY: CreateAclDeny,
            CommandEnum.CREATE_EXT_ACL_PERMIT: CreateExtAclPermit,
            CommandEnum.CREATE_EXT_ACL_DENY: CreateExtAclDeny,
            # Set
            CommandEnum.SET_SPEED: SetSpeed,
            CommandEnum.SET_DUPLEX: SetDuplex,
            CommandEnum.SET_VLAN: SetVlan,
            CommandEnum.SET_POLICE_IN: SetPoliceIn,
            CommandEnum.SET_POLICE_OUT: SetPoliceOut,
            CommandEnum.SET_ACL_IN: SetAclIn,
            CommandEnum.SET_ACL_OUT: SetAclOut,
            CommandEnum.SET_PORT_SECURITY_MAXIMUM: SetPortSecurityMaximum,
            CommandEnum.SET_PORT_SECURITY_VIO_PROTECT: SetPortSecurityVioProtect,
            CommandEnum.SET_PORT_SECURITY_VIO_RESTRICT: SetPortSecurityVioRestrict,
            CommandEnum.SET_PORT_SECURITY_VIO_SHUTDOWN: SetPortSecurityVioShutdown,
            CommandEnum.SET_INTERFACE_DESCRIPTION: SetInterfaceDescription,
            # Unset
            CommandEnum.UNSET_POLICE_IN: UnsetPoliceIn,
            CommandEnum.UNSET_POLICE_OUT: UnsetPoliceOut,
            # Clear
            CommandEnum.CLEAR_PORT_SECURITY_ALL: ClearPortSecurityAll,
            CommandEnum.CLEAR_POLICE: ClearPolice,
            # Show
            CommandEnum.SHOW_PMAP_LIST: ShowPmapList,
            CommandEnum.SHOW_PMAP_INT_LIST: ShowPmapIntList,
            CommandEnum.SHOW_RUNNING_CONFIG: ShowRunningConfig,
            CommandEnum.SHOW_PORT_SECURITY_ADDRESS: ShowPortSecurityAddress,
            CommandEnum.SHOW_SNMP_HOST: ShowSnmpHost,
            # Other
            # !!!!! This is a dangerous operation !!!!!
            CommandEnum.CUSTOM: Custom,
        }

        # Undo command Stack (isolated by user id).
        self.__undo_commands_stack: Dict[int, List[Dict[str, Command or list]]] = defaultdict(list)

        # Undo command Stack capacity limit (Only store at most "three" recent historical operations).
        self.__UNDO_COMMAND_STACK_CAPACITY_LIMIT: int = 3

    def execute_command(
            self,
            user_id: int or None,
            device_id: str or None,
            device_name: str or None,
            command_enum: CommandEnum,
            connect_info: tuple,
            command_info: list = None
    ) -> (bool, list, str):
        """
        Execute command and return the "result and device response".

        Because we need to satisfy the behavior of undo (isolate by user id),
        so we have to make each command instance independent (isolate each command instance),
        to ensure that the commands will not affect each other,
        therefore the command instance cannot be reused here.
        """

        # The "value" type of the "self.__commands" dictionary is non-instance,
        # it needs to be instantiated through "()" to use.
        command: Command = self.__commands[command_enum](connect_info, command_info)

        # Execute.
        is_success, recv_list, msg = command.execute()

        # If the execution is successful, save the command to "undo_commands_stack",
        # but when the first three parameters are "None",
        # it means that the Command does not need or cannot be revoked,
        # and it will not be stored to "undo_commands_stack".
        if is_success and user_id is not None and device_id is not None and device_name is not None:
            self.__undo_commands_stack[user_id].append({
                "device_id": device_id,
                "device_name": device_name,
                "command": command,
                "recv_list": recv_list
            })

            # Limit the number or undo commands.
            if len(self.__undo_commands_stack[user_id]) > self.__UNDO_COMMAND_STACK_CAPACITY_LIMIT:
                self.__undo_commands_stack[user_id].pop(0)

        # Return execution results.
        return is_success, recv_list, msg

    def undo_command(self, user_id: int) -> (bool, list, str, str, str):
        """
        Undo command and return the "result and device response".

        The undo command Stack will be isolated by user id.
        """

        # Get the command to be revoked.
        try:
            undo_command_info: dict = self.__undo_commands_stack[user_id].pop()
        except IndexError:
            return False, [], "Failed to obtain the command to be revoked.", "NO_DEVICE_ID", "NO_DEVICE_NAME"

        command: Command = undo_command_info["command"]

        # Execute.
        try:
            is_success, recv_list, msg = command.undo()
        except NotImplementedError as e:
            return False, [], e, undo_command_info["device_id"], undo_command_info["device_name"]

        # Return execution results.
        return is_success, recv_list, msg, undo_command_info["device_id"], undo_command_info["device_name"]

    def get_undo_command_stack(self, user_id: int) -> list:
        """
        Return Stack content for users to peek it.
        """

        undo_commands_stack: List[Dict[str, list]] = [
            {
                "device_name": i["device_name"],
                "recv_list": i["recv_list"]
            } for i in self.__undo_commands_stack[user_id]
        ]

        return undo_commands_stack

    def clear_undo_command_stack(self, user_id: int) -> bool:
        """
        Clear the command Stack for the specified user id.
        """

        self.__undo_commands_stack[user_id].clear()

        return True


if __name__ == '__main__':
    remote_controller: RemoteController = RemoteController()
