from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel

agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=HfApiModel("gpt2"))


agent.run("Write Python code using Selenium to: 1. Open Naukri.com.")
