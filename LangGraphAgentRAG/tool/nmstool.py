from langchain.tools import tool

class NMSTool:
    @staticmethod
    def open_port(ip: str, interface_name: str) -> str:
        """
        這個工具用於開啟指定網路設備交換器的特定埠號，
        適用於用戶想開啟指定網路設備交換器特定埠號之場景。

        :param ip: 請傳入 IP 字串。
        :type ip: str

        :param interface_name: 請傳入網路設備埠號。
        :type interface_name: str

        :return: 是否成功執行網管指令。
        :rtype: str

        :適用場景:
            - 戶想開啟指定網路設備交換器特定埠號。

        :調用案例:
            - 開啟 173.3.16.111 交換器的 gi1/0/4 埠
            - 開啟 173.3.16.111 的 gi1/0/4
        """

        return f"設備 {ip} 的 {interface_name} 埠開啟指令已成功執行"

    @staticmethod
    def close_port(ip: str, interface_name: str) -> str:
        """
        這個工具用於關閉指定網路設備交換器的特定埠號，
        適用於用戶想關閉指定網路設備交換器特定埠號之場景。

        :param ip: 請傳入 IP 字串。
        :type ip: str

        :param interface_name: 請傳入網路設備埠號。
        :type interface_name: str

        :return: 是否成功執行網管指令。
        :rtype: str

        :適用場景:
            - 戶想關閉指定網路設備交換器特定埠號。

        :調用案例:
            - 關閉 173.3.16.111 交換器的 gi1/0/4 埠
            - 關閉 173.3.16.111 的 gi1/0/4
        """

        return f"設備 {ip} 的 {interface_name} 埠關閉指令已成功執行"

    @classmethod
    def get_tools(cls):
        return [
            tool(cls.open_port),
            tool(cls.close_port),
        ]
