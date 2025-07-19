import requests

from langchain.tools import tool

from config import config

class PATool:
    @staticmethod
    def is_employee_present(employee_id: str) -> str:
        """
        這個工具用於查詢指定員工編號員工即時到勤資訊，
        適用於用戶想了解指定員工編號員工的即時到勤資訊之場景。

        :param employee_id: 員工編號。
        :type employee_id: str

        :return: 指定員工編號員工的即時到勤資訊。
        :rtype: str

        :適用場景:
            - 用戶詢問指定員工編號員工之到勤。

        :調用案例:
            - 員工 1113508 今天有來嗎
            - 承辦人 1113508 現在在嗎
        """

        response = requests.get(
            f"http://{config.HOST}:8888/api/employee/present", params={"employee_id": employee_id}
        )

        is_present = response.json()

        return f"員工編號為 {employee_id} 的同仁，今日{'有' if is_present else '沒'}來上班。"

    @classmethod
    def get_tools(cls):
        return [
            tool(cls.is_employee_present),
        ]
