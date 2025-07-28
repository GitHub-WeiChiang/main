from langchain.tools import tool
from pydantic import BaseModel, Field

from cscocligen.InterfaceMode import InterfaceMode
from config import config

class NMSTool:
    @staticmethod
    def open_port(ip: str, port: str) -> str:
        """
        這個工具用於開啟指定網路設備交換器的特定埠號，
        適用於用戶想開啟指定網路設備交換器特定埠號之場景。

        :param ip: 請傳入 IP 字串。
        :type ip: str

        :param port: 請傳入網路設備埠號。
        :type port: str

        :return: 是否成功執行網管指令。
        :rtype: str

        :適用場景:
            - 用戶想開啟指定網路設備交換器特定埠號。

        :調用案例:
            - 開啟 xxx.xxx.xxx.xxx 交換器的 gi1/0/4 埠
            - 開啟 xxx.xxx.xxx.xxx 的 gi1/0/4
        """

        is_success, recv_list, msg = InterfaceMode(port).no_shut().exec(config.CSCO_T_SW_CONN_INFO)

        return f"設備 {ip} 的 {port} 埠開啟指令執行 {'成功' if is_success else '失敗'}"

    @staticmethod
    def close_port(ip: str, port: str) -> str:
        """
        這個工具用於關閉指定網路設備交換器的特定埠號，
        適用於用戶想關閉指定網路設備交換器特定埠號之場景。

        :param ip: 請傳入 IP 字串。
        :type ip: str

        :param port: 請傳入網路設備埠號。
        :type port: str

        :return: 是否成功執行網管指令。
        :rtype: str

        :適用場景:
            - 用戶想關閉指定網路設備交換器特定埠號。

        :調用案例:
            - 關閉 xxx.xxx.xxx.xxx 交換器的 gi1/0/4 埠
            - 關閉 xxx.xxx.xxx.xxx 的 gi1/0/4
        """

        is_success, recv_list, msg = InterfaceMode(port).shut().exec(config.CSCO_T_SW_CONN_INFO)

        return f"設備 {ip} 的 {port} 埠關閉指令執行 {'成功' if is_success else '失敗'}"

    @staticmethod
    def set_description(ip: str, port: str, desc: str) -> str:
        """
        這個工具用於添加指定網路設備交換器的特定埠號功能描述，
        適用於用戶想添加指定網路設備交換器特定埠號功能描述之場景。

        :param ip: 請傳入 IP 字串。
        :type ip: str

        :param port: 請傳入網路設備埠號。
        :type port: str

        :param desc: 請傳入要添加的功能描述。
        :type desc: str

        :return: 是否成功執行網管指令。
        :rtype: str

        :適用場景:
            - 用戶想關閉指定網路設備交換器特定埠號。

        :調用案例:
            - 幫我將 xxx.xxx.xxx.xxx 交換器的 gi1/0/4 埠添加以下描述 This is a test interface
            - 幫我在 xxx.xxx.xxx.xxx 的 gi1/0/4 上添加下方敘述 This interface is not be used
        """

        is_success, recv_list, msg = InterfaceMode(port).description(desc).exec(config.CSCO_T_SW_CONN_INFO)

        return f"設備 {ip} 的 {port} 埠功能描述添加指令執行 {'成功' if is_success else '失敗'}"

    @classmethod
    def get_tools(cls):
        return [
            tool(cls.open_port, args_schema=OpenPortArgsSchema),
            tool(cls.close_port, args_schema=ClosePortArgsSchema),
            tool(cls.set_description, args_schema=SetDescriptionSchema),
        ]

class OpenPortArgsSchema(BaseModel):
    ip: str = Field(description="網路設備交換器的 IP 位址")
    port: str = Field(description="要開啟的埠號")

class ClosePortArgsSchema(BaseModel):
    ip: str = Field(description="網路設備交換器的 IP 位址")
    port: str = Field(description="要關閉的埠號")

class SetDescriptionSchema(BaseModel):
    ip: str = Field(description="網路設備交換器的 IP 位址")
    port: str = Field(description="要設定功能描述的埠號")
    desc: str = Field(description="功能描述內容")
