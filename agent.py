import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent

# Load environment variables
load_dotenv()

# Initialize model
llm = ChatOpenAI(model="gpt-4o-mini")

# ---------------------------
# 🧠 System Prompt
# ---------------------------
system_prompt = """You are a helpful personal research assistant.
You help users answer questions, perform calculations, and analyze text.

Be concise, clear, and accurate.
Use tools when necessary.
If you don't know something, say so honestly.
"""

# ---------------------------
# 🔧 Custom Tools
# ---------------------------

@tool
def calculator(expression: str) -> str:
    """Evaluate a simple math expression."""
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {str(e)}"


@tool
def word_counter(text: str) -> str:
    """Count the number of words in a string."""
    try:
        return f"Word count: {len(text.split())}"
    except Exception as e:
        return f"Error: {str(e)}"


@tool
def simple_search(query: str) -> str:
    """Mock search tool."""
    try:
        return f"Search results for '{query}': (placeholder result)"
    except Exception as e:
        return f"Error: {str(e)}"


# ---------------------------
# 🤖 Create Agent
# ---------------------------

tools = [calculator, word_counter, simple_search]
agent = create_react_agent(llm, tools, prompt=system_prompt)

# ---------------------------
# ▶️ Run Agent Loop
# ---------------------------

if __name__ == "__main__":
    print("Personal Research Assistant (type 'exit' to quit)\n")

    messages = []

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        messages.append(("user", user_input))

        try:
            response = agent.invoke({"messages": messages})
            agent_reply = response["messages"][-1].content

            print("Agent:", agent_reply)

            messages.append(("assistant", agent_reply))

        except Exception as e:
            print("Error:", str(e))
