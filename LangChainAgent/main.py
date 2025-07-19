from langchain_ollama import ChatOllama
from langchain.agents import initialize_agent, AgentType
from langchain.agents import Tool

# 定義本地可執行的函數
def get_weather(location: str) -> str:
    """模擬查詢天氣的 API"""
    return f"The current weather in {location} is sunny with 25°C."

def get_time(location: str) -> str:
    """模擬查詢當地時間的 API"""
    return f"The current time in {location} is 3:00 PM."

# 封裝本地方法為 LangChain 工具
tools = [
    Tool(
        name="GetWeather",
        func=get_weather,
        description="查詢指定地點的天氣資訊。輸入應該是城市名稱，例如 'Tokyo' 或 'New York'。",
    ),
    Tool(
        name="GetTime",
        func=get_time,
        description="查詢指定地點的當前時間。輸入應該是城市名稱，例如 'London' 或 'Paris'。",
    ),
]

# 初始化 Ollama 作為 LLM
llm = ChatOllama(model="gemma2:9b")  # 確保你的模型名稱正確

# 建立 LangChain Agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  # 讓 LLM 依據工具描述自行決定使用何種工具
    verbose=True  # 顯示詳細過程
)

if __name__ == "__main__":
    while True:
        user_input = input("\nAsk me something (type 'exit' to quit): ")
        if user_input.lower() == "exit":
            break

        response = agent.run(user_input)
        print(f"\n🤖 Response: {response}")
