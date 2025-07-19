import datetime

from langchain.tools import tool

class CommonTool:
    @staticmethod
    def get_current_time(query: str = "") -> str:
        """
        這個工具用於查詢即時的日期與時間資訊，
        適用於用戶想了解當前的日期與時間之場景。

        :param query: 請傳入空字串。
        :type query: str

        :return: 系統當前的日期與時間資訊。
        :rtype: str

        :適用場景:
            - 用戶詢問當前日期。
            - 用戶詢問當前時間。
            - 用戶詢問當前日期與時間。

        :調用案例:
            - 今天幾號
            - 現在幾點
            - 今日何日今夕何夕
            - 現在幾點幾分
            - 今天幾月幾號
        """

        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def get_weather(month: int, date: int) -> str:
        """
        這個工具用於查詢特定月分與日期的天氣資訊，
        適用於用戶想了解特定的月分與日期天氣之場景。

        :param month: 月份。
        :type month: int

        :param date: 日期。
        :type month: int

        :return: 特定的月分與日期天氣資訊。
        :rtype: str

        :適用場景:
            - 用戶詢問指定月份日期之天氣。

        :調用案例:
            - 四月二十五日的天氣如何
            - 1/23 的天氣如何
        """

        print(month, date)
        return f"{month} 月 {date} 日的天氣: 當天為大熱天，氣溫約一百零五度，滴滴青春的蒸餾水。"

    @classmethod
    def get_tools(cls):
        return [
            tool(cls.get_current_time),
            tool(cls.get_weather),
        ]
