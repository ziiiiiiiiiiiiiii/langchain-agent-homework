## 1. Project Title & Description (2-3 sentences) - What does this agent do?

This agent uses Langchain and LangGraph to help uses with everyday research tasks using custom tools and the ReAct pattern (Reason + Act). It runs locally and uses good software engineering practices like a virtual environment, requirements, and Git.

## 2. Tools Implemented (brief description of each)
An interactive conversation loop that keeps a memory of previous messages.
Three custom tools:
- Calculator: Evaluate simple math expressions
- Word Counter: Count words in a text
- Simple search: Does a search of the internet and returns brief results

I chose these because they are basic tasks used in many research assignments.

## 3. How to Run

Step-by-step instructions so anyone can clone and run your agent:
Setup
1. Clone the repository:

git clone https://github.com/YOUR_USERNAME/langchain-agent-homework.git
cd langchain-agent-homework

2. Create and activate a virtual environment:

python -m venv venv

macOS/Linux:
source venv/bin/activate

Windows (Git Bash):
source venv/Scripts/activate

3. Create a `.env` file in the project root and enter:

OPENAI_API_KEY=your-key-here

4. Install dependencies:

pip install -r requirements.txt

## Usage

Run the agent interactively:

python agent.py

Type your queries in the terminal. Example commands:
* `What is 25 * 4 + 10?`
* `Count the words in: LangChain is really powerful`
* `Search for benefits of exercise`

Type `exit` to quit.

4. Example Conversation
<img width="1445" height="682" alt="Screenshot 2026-04-07 203340" src="https://github.com/user-attachments/assets/e7550a55-9cdf-4ad9-a049-e45af6254e66" />

5. Reflection (3-5 sentences)

- What was the most interesting thing you learned?

I didn't know it was this easy to create a custom agent and run it locally on my PC with just an API key and a Python script that isn't too long.

- What was the hardest part?

I'm still not that used to Git as I am not really a programmer, so each time I have to look up commands and sometimes undo them when I make a mistake.

- What would you add next if you had more time?

I would add more tools, and find a way to integrate this into Microsoft Word, where I and most people would be doing our research assignments.
