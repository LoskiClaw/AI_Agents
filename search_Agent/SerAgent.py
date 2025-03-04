# 导入LangChain Hub
from langchain import hub 
# 从LangChain Hub中获取ReAct的提示
prompt = hub.pull("hwchase17/react")
print(prompt)
# 导入OpenAI 
from langchain_openai import OpenAI

import os
import dotenv
# 从.env文件中读取API Key  
dotenv.load_dotenv()
LLM_API_KEY = os.getenv("LLM_API_KEY")
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

# 选择要使用的大模型
llm = OpenAI(model='deepseek-chat', api_key=LLM_API_KEY, base_url="https://api.deepseek.com/beta")
# 导入SerpAPIWrapper即工具包
from langchain_community.utilities import SerpAPIWrapper 
from langchain.tools import Tool
# 实例化SerpAPIWrapper 
search = SerpAPIWrapper(serpapi_api_key=SERPAPI_API_KEY) 
#准备工具列表
tools = [
    Tool(name="Search", func=search.run, description="当大模型没有相关知识时，用于搜索知识"), 
]
# 导入create_react_agent功能
from langchain.agents import create_react_agent 
# 构建ReAct Agent 
agent = create_react_agent(llm, tools, prompt) 
# 导入AgentExecutor
from langchain.agents import AgentExecutor 
# 创建Agent执行器并传入Agent和工具
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True) 
# 调用AgentExecutor 
agent_executor.invoke({"input": "当前Agent最新研究进展是什么？"})