import os
import dotenv
# 从.env文件中读取API Key  
dotenv.load_dotenv()
LLM_API_KEY = os.getenv("LLM_API_KEY")

from openai import OpenAI
client = OpenAI(api_key=LLM_API_KEY, base_url="https://api.deepseek.com/")
# 创建一个对话
response = client.chat.completions.create(
    model="deepseek-chat", 
    response_format={ "type": "json_object"}, 
    messages=[
        {"role": "system",   "content": "您是一个帮助用户了解鲜花信息的智能助手, 并能够输出JSON格式的内容。"}, 
        {"role": "user",     "content": "生日送什么花最好？"}, 
        {"role":"assistant", "content": "玫瑰花是生日礼物的热门选择。"}, 
        {"role": "user",     "content": "送货需要多长时间？"}
    ],
    max_tokens=1024,
    temperature=0.7,
    stream=False
)

print(response)
