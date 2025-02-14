import json
import re
import ollama

# 定義本地可執行的函數
def get_weather(location):
    return f"The current weather in {location} is sunny with 25°C."

def get_time(location):
    return f"The current time in {location} is 3:00 PM."

# 可被 LLM 呼叫的方法映射
api_methods = {
    "get_weather": get_weather,
    "get_time": get_time
}

# 設定提示詞，要求 LLM 輸出 JSON 格式
prompt = """
You are an assistant that provides structured responses in JSON format.

Always return responses strictly in the following JSON format:
{
  "action": "function_name",
  "parameters": {
    "location": "city_name"
  }
}

Examples:
- "What's the weather in New York?" =>
  {
    "action": "get_weather",
    "parameters": {
      "location": "New York"
    }
  }
- "What time is it in London?" =>
  {
    "action": "get_time",
    "parameters": {
      "location": "London"
    }
  }

DO NOT include markdown, only return pure JSON. DO NOT add explanations.
"""

def clean_json_output(llm_output):
    """ 去除 Markdown JSON 標記 (```json ... ```) """
    match = re.search(r"```json\n(.*?)\n```", llm_output, re.DOTALL)
    if match:
        return match.group(1).strip()  # 提取 JSON 內容
    return llm_output.strip()  # 直接回傳（如果沒有 Markdown 標記）

def prompt_to_action(user_input):
    response = ollama.chat(model='gemma2:9b', messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": user_input}
    ])

    # 取得 LLM 回應內容
    llm_output = response['message']['content']
    print(f"Raw LLM Output: {llm_output}")

    # 清理 JSON 回應
    clean_output = clean_json_output(llm_output)
    print(f"Cleaned JSON Output: {clean_output}")

    try:
        parsed_output = json.loads(clean_output)
        action = parsed_output.get("action")
        parameters = parsed_output.get("parameters", {})

        # 執行對應方法
        if action in api_methods and "location" in parameters:
            result = api_methods[action](parameters["location"])
            print(f"Function Output: {result}")
        else:
            print("Invalid action or missing parameters.")
    except json.JSONDecodeError:
        print("Failed to parse cleaned JSON response.")

if __name__ == "__main__":
    user_query = input("Ask me something: ")
    prompt_to_action(user_query)
