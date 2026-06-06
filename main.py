# pip install -qU deepagents langchain-google-genai
from deepagents import create_deep_agent
import os

os.environ["GOOGLE_API_KEY"] = "AQ.Ab8RN6KIaxSELvYS4-Oh7PZn4XMpITvMcYPPlR6iUkJBgbrBJA"


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

# Run the agent
print(
    agent.invoke(
        {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
    )
)
