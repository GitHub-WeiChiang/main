import pprint as pp

from config import config

if __name__ == "__main__":
    # ------------------------------------------------------------

    # from cscocligen.InterfaceMode import InterfaceMode

    # print(InterfaceMode("gi1/0/4").shut().build())
    # print(InterfaceMode("gi1/0/4").shut().exec(config.CSCO_T_SW_CONN_INFO))

    # print(InterfaceMode("gi1/0/4").no_shut().build())
    # print(InterfaceMode("gi1/0/4").no_shut().exec(config.CSCO_T_SW_CONN_INFO))

    # ------------------------------------------------------------

    # from llm.chathistoryhandler import ChatHistoryHandler
    #
    # chat_histories = [
    #     {"role": "user", "content": "xxx"},
    #     {"role": "bot", "content": "xxx"},
    #     {"role": "user", "content": "xxx"},
    #     {"role": "bot", "content": "xxx"}
    # ]
    #
    # question = "xxx"
    #
    # messages = ChatHistoryHandler.generate_message(chat_histories, question)
    #
    # pp.pprint(messages)

    # ------------------------------------------------------------

    pass

"""
{
  "category": "測試專用",
  "question": "給我全彩公雞圖",
  "chat_histories": []
}
"""

"""
{
  "category": "測試專用",
  "question": "給我所有公雞的參數表格",
  "chat_histories": []
}
"""

"""
{
  "category": "",
  "question": "請問我是誰",
  "chat_histories": [
	{
		"role": "user",
		"content": "您好，我是野原新之助。"
	},
	{
		"role": "bot",
		"content": "您好，野原新之助先生！\n\n很高興能為您服務。"
	},
	{
		"role": "user",
		"content": "您好，我今年五歲。"
	},
	{
		"role": "bot",
		"content": "您好！很高興認識您。您今年五歲，真是個可愛的小朋友！"
	}
  ]
}
"""

"""
{
  "category": "",
  "question": "請問我幾歲",
  "chat_histories": [
	{
		"role": "user",
		"content": "您好，我是野原新之助。"
	},
	{
		"role": "bot",
		"content": "您好，野原新之助先生！\n\n很高興能為您服務。"
	},
	{
		"role": "user",
		"content": "您好，我今年五歲。"
	},
	{
		"role": "bot",
		"content": "您好！很高興認識您。您今年五歲，真是個可愛的小朋友！"
	}
  ]
}
"""

"""
{
  "category": "",
  "question": "幫我關閉 xxx.xxx.xxx.xxx 的gi1/0/4",
  "chat_histories": [
	{
		"role": "user",
		"content": "幫我關閉 xxx.xxx.xxx.xxx 的 gi1/0/1"
	},
	{
		"role": "bot",
		"content": "設備 xxx.xxx.xxx.xxx 的 gi1/0/1 埠已成功關閉。"
	},
	{
		"role": "user",
		"content": "幫我關閉 xxx.xxx.xxx.xxx 的 gi1/0/2"
	},
	{
		"role": "bot",
		"content": "設備 xxx.xxx.xxx.xxx 的 gi1/0/2 埠已成功關閉。"
	},
	{
		"role": "user",
		"content": "幫我關閉 xxx.xxx.xxx.xxx 的 gi1/0/3"
	},
	{
		"role": "bot",
		"content": "設備 xxx.xxx.xxx.xxx 的 gi1/0/3 埠已成功關閉。"
	}
  ]
}
"""
