import requests

from langchain.tools import tool

from config import config

class PATool:
    @staticmethod
    def is_employee_present(employee_name: str) -> str:
        """
        這個工具用於查詢一位指定員工即時到勤資訊，
        適用於用戶想了解一位指定員工的即時到勤資訊之場景。

        :param employee_name: 一位員工的姓名。
        :type employee_name: str

        :return: 指定員工的即時到勤資訊。
        :rtype: str

        :適用場景:
            - 用戶詢問指定員工之到勤。

        :調用案例:
            - 員工 xxx 今天有來嗎
            - 承辦人 xxx 現在在嗎
        """

        response = requests.get(
            f"http://{config.HOST}:8888/api/employee/present", params={"employee_name": employee_name}
        )

        is_present = response.json()

        return f"員工 {employee_name} 今日 {'有' if is_present else '沒'} 來上班。"

    @classmethod
    def get_tools(cls):
        return [
            tool(cls.is_employee_present),
        ]
