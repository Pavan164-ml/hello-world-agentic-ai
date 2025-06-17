# agent.py
from openai import OpenAI
from tools import AVAILABLE_TOOLS # Import our tools

# --- SETUP ---
# Point the OpenAI client to your local Ollama server
# The 'api_key' is not used by Ollama but the library requires it to be set.
client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='ollama',  # required, but unused
)

# --- PROMPT DEFINITION ---
# This master prompt is slightly tweaked for open-source models, which sometimes need more explicit instructions.
AGENT_PROMPT = """
You are a helpful AI assistant that can use tools to answer questions.
You have access to the following tools:

- `web_search(query: str)`: Use this to search the web for up-to-date information.
- `finish(answer: str)`: Use this when you have the final answer to the user's question.

Your thought process MUST be in the following format. Do not deviate from this format.

Thought: Analyze the user's question and the previous steps. Decide what to do next.
Action: Choose one of the available tools.
Action Input: Provide the input for the chosen tool.

You will repeat this cycle until you have the final answer.
After a tool is executed, you will see the "Observation" and then you must produce a new "Thought, Action, Action Input" block.
When you have the final answer, use the `finish` tool.

---
User Question: {user_question}
---
{agent_scratchpad}
"""

def run_agent(user_question: str):
    """
    The main agentic loop.
    """
    agent_scratchpad = ""

    while True:
        # 1. PREPARE THE PROMPT
        full_prompt = AGENT_PROMPT.format(
            user_question=user_question,
            agent_scratchpad=agent_scratchpad
        )

        # 2. CALL THE LOCAL LLM
        print("--- Calling local LLM (Phi-3)... ---")
        response = client.chat.completions.create(
            # This is the model name you used in 'ollama pull'
            model="phi3:mini",
            messages=[{"role": "user", "content": full_prompt}],
            temperature=0,
        )
        llm_output = response.choices[0].message.content.strip()
        print(llm_output)

        agent_scratchpad += llm_output + "\n"

        # 3. PARSE THE LLM's OUTPUT
        try:
            action = llm_output.split("Action:")[1].split("Action Input:")[0].strip()
            action_input = llm_output.split("Action Input:")[1].strip()
        except IndexError:
            print("--- ERROR: Could not parse LLM output. Retrying... ---")
            continue

        # 4. EXECUTE THE CHOSEN TOOL
        if action in AVAILABLE_TOOLS:
            tool_function = AVAILABLE_TOOLS[action]

            if action == "finish":
                print("--- Agent finished. ---")
                return action_input

            observation = tool_function(action_input)
            agent_scratchpad += f"Observation: {observation}\n"
        else:
            print(f"--- ERROR: Unknown action '{action}'. Retrying... ---")
            agent_scratchpad += f"Observation: Error - Unknown action '{action}'.\n"

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # USER_QUESTION = "Who is the current chancellor of Germany, and what is the population of Germany's capital city?"
    USER_QUESTION = input("Please ennter your question :\n")
    final_answer = run_agent(USER_QUESTION)
    print("\n\n===== FINAL ANSWER =====")
    print(final_answer)