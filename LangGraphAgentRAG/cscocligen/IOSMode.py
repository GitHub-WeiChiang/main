import paramiko
import time
import socket

from config import config

class IOSMode:
    def __init__(self, commands = None):
        self.__commands = [] if commands is None else commands

    def _append_command(self, command):
        self.__commands.append(command)

    def exec(self, connect_info, wait_time=config.REMOTE_CTRL_COMMAND_INTERVAL_TIME):
        is_success = True
        recv_list = []
        msg = "Command send successfully."

        try:
            with paramiko.SSHClient() as ssh_client:
                ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh_client.connect(
                    connect_info[0], connect_info[1], connect_info[2], connect_info[3],
                    look_for_keys=False, allow_agent=False, timeout=config.SSH_TIMEOUT
                )

                remote = ssh_client.invoke_shell()

                for command in self.__commands:
                    remote.send(command)

                    time.sleep(wait_time)
                    wait_time = config.REMOTE_CTRL_COMMAND_INTERVAL_TIME

                    recv = list(filter(None, remote.recv(66000).decode("utf-8").split("\r\n")))

                    recv[0] = recv[0].replace(
                        "\x08\x08\x08\x08\x08\x08\x08\x08\x08        \x08\x08\x08\x08\x08\x08\x08\x08\x08", ""
                    )

                    if "--More--" in recv[-1]:
                        recv_list = recv_list + recv[0:-1]
                        self.__commands.append(" ")
                        continue

                    recv_list = recv_list + recv
        except paramiko.ssh_exception.NoValidConnectionsError:
            is_success = False
            msg = "Failed to establish a valid SSH connection."
        except paramiko.ssh_exception.AuthenticationException:
            is_success = False
            msg = "Authentication failed."
        except paramiko.ssh_exception.ChannelException:
            is_success = False
            msg = "Channel error."
        except paramiko.ssh_exception.SSHException:
            is_success = False
            msg = "SSH error."
        except socket.timeout:
            is_success = False
            msg = "SSH operation timed out."
        except Exception:
            is_success = False
            msg = "Other exception."
        finally:
            return is_success, recv_list, msg

    def build(self):
        return self.__commands
