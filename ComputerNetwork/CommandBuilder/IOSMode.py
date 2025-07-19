# Import paramiko module.
import paramiko
# Import time module.
import time
# Import socket module.
import socket

# Config class.
from Config import Config
# Interval time of remote control command send.
# self.REMOTE_CTRL_COMMAND_INTERVAL_TIME: float = 1
# SSH timeout.
# self.SSH_TIMEOUT: float = 5


class IOSMode:
    """
    Implement Stream API with Builder Pattern.
    """

    def __init__(self, commands: list = None):
        self.__commands: list = [] if commands is None else commands

    # ============================================================
    # ---------------------- Protected Func ----------------------
    # ============================================================

    def _append_command(self, command: str):
        # Add Cisco IOS command.
        self.__commands.append(command)

    # ============================================================
    # -------------------- Terminal Operation --------------------
    # ---------- At the end of streams you must call it ----------
    # ============================================================

    # Connect to the remote device via ssh and execute.
    def exec(
            self, connect_info: tuple, wait_time: int = Config().REMOTE_CTRL_COMMAND_INTERVAL_TIME
    ) -> (bool, list, str):
        # Return value.
        is_success: bool = True
        recv_list: list = []
        msg: str = "Command send successfully."

        try:
            # Use context manager to control SSHClient().
            with paramiko.SSHClient() as ssh_client:
                # Sey policy to allow when connecting to servers without a known host key.
                ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                # Connect to an SSH server and authenticate to it.
                ssh_client.connect(
                    connect_info[0], connect_info[1], connect_info[2], connect_info[3],
                    look_for_keys=False, allow_agent=False, timeout=Config().SSH_TIMEOUT
                )

                # Start an interactive shell session on the SSH server.
                remote = ssh_client.invoke_shell()

                # Sent each command.
                for command in self.__commands:
                    remote.send(command)

                    # The sleep() method must be executed after each command is sent,
                    # It is not possible to wait through the following code:
                    #
                    #     while not remote.recv_ready():
                    #         pass
                    #
                    # Because the device may return a specific string first,
                    # such as the "Building configuration..." string when sending the "sh running-config" command.

                    # Wait for it to finish.
                    time.sleep(wait_time)
                    # I know it's ugly to write like this,
                    # but some operations must wait for the network device to response,
                    # for example, get the device running-config,
                    # the device takes a long time to reply to the first piece of content,
                    # so we have to set a longer time for the first time,
                    # then we can use the preset wait time.
                    wait_time = Config().REMOTE_CTRL_COMMAND_INTERVAL_TIME

                    # Collect responses from remote devices.
                    # Why is it set to "66000" ?
                    # Because "Liu liu da shun".
                    recv: list = list(filter(None, remote.recv(66000).decode("utf-8").split("\r\n")))

                    # Replace the "Backspace" character.
                    recv[0] = recv[0].replace(
                        "\x08\x08\x08\x08\x08\x08\x08\x08\x08        \x08\x08\x08\x08\x08\x08\x08\x08\x08", ""
                    )

                    # Handle "more" response.
                    if "--More--" in recv[-1]:
                        recv_list = recv_list + recv[0:-1]
                        self.__commands.append(" ")
                        continue

                    # Collect results.
                    recv_list = recv_list + recv
        except paramiko.ssh_exception.NoValidConnectionsError:
            # 無法建立有效的 SSH 連線
            is_success = False
            msg = "Failed to establish a valid SSH connection."
        except paramiko.ssh_exception.AuthenticationException:
            # 身分驗證失敗
            is_success = False
            msg = "Authentication failed."
        except paramiko.ssh_exception.ChannelException:
            # 通道錯誤
            is_success = False
            msg = "Channel error."
        except paramiko.ssh_exception.SSHException:
            # SSH 錯誤
            is_success = False
            msg = "SSH error."
        except socket.timeout:
            # SSH 操作超時
            is_success = False
            msg = "SSH operation timed out."
        except Exception:
            # 其它例外
            is_success = False
            msg = "Other exception."
        finally:
            # Return the result.
            return is_success, recv_list, msg

    # Get the build result of the command array.
    def build(self) -> list:
        return self.__commands
