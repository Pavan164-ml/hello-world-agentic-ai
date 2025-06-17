# Simple Local AI Agent - Hello World

This project is a hands-on, "Hello World" introduction to building an agentic AI framework. The goal is to demystify how AI agents work by building one from scratch that can reason and use tools to solve a multi-step problem.

The entire framework is designed to run locally on your own machine using entirely free and open-source tools. **No API keys, no subscriptions, and no cloud costs are required.**

The agent is designed to answer a multi-step question like: *"Who is the current chancellor of Germany, and what is the population of Germany's capital city?"*

## Key Features

-   **100% Free & Local:** Runs entirely on your computer. Your data stays private, and there's no risk of incurring costs.
-   **OpenAI API Compatible:** By using [Ollama](https://ollama.com/), the agent interacts with a local LLM using the standard `openai` Python library. This makes your skills directly transferable to commercial models.
-   **Simple & Understandable:** The code is written to be as clear as possible, with a focus on the core **Reason-Act-Observe** loop, avoiding complex abstractions.
-   **Extensible:** The design makes it easy to add new custom tools (e.g., a calculator, file reader, or code executor) to expand the agent's capabilities.

## Technology Stack

-   **LLM Server:** [**Ollama**](https://ollama.com/) - For easily downloading and serving open-source LLMs locally.
-   **LLM Model:** [**Phi-3 Mini**](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct) - A powerful and efficient small language model from Microsoft that runs well on consumer hardware.
-   **Core Logic:** **Python 3**
-   **LLM Interaction:** `openai` Python library
-   **Web Search Tool:** `duckduckgo-search` Python library (no API key needed).

---

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have the following installed on your system:
1.  **Python 3.8+** ([Download here](https://www.python.org/downloads/))
2.  **Ollama** ([Download here](https://ollama.com/))

### Installation & Setup

1.  **Clone the Repository** (or download the files)
    ```bash
    git clone https://github.com/your-username/local-agent-project.git
    cd local-agent-project
    ```
    *(If you didn't use git, just navigate to the project folder you created).*

2.  **Download the LLM with Ollama**
    Open your terminal and pull the `phi3:mini` model. This will download the model and make it available for Ollama to serve.
    ```bash
    ollama pull phi3:mini
    ```
    *(Ollama will run as a background service after installation).*

3.  **Create and Activate a Python Virtual Environment**
    It's highly recommended to use a virtual environment to keep project dependencies isolated.

    ```bash
    # Create the environment
    python -m venv venv

    # Activate the environment
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```
    Your terminal prompt should now be prefixed with `(venv)`.

4.  **Install Python Dependencies**
    ```bash
    pip install openai duckduckgo-search
    ```

### Running the Agent

With your virtual environment activated, run the main agent script:

```bash
python agent.py
