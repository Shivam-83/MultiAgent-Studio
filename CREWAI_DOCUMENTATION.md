# 📚 CrewAI Technical Documentation

Complete guide to all CrewAI components, tools, and implementation used in this project.

---

## 📑 Table of Contents

1. [CrewAI Overview](#crewai-overview)
2. [Core Components](#core-components)
3. [Agent Configuration](#agent-configuration)
4. [Task Configuration](#task-configuration)
5. [Crew Management](#crew-management)
6. [LLM Integration](#llm-integration)
7. [Tools & Extensions](#tools--extensions)
8. [Code Examples](#code-examples)

---

## 🎯 CrewAI Overview

### What is CrewAI?

CrewAI is a framework for orchestrating role-based autonomous AI agents. It enables you to create agents that can work together to complete complex tasks.

**Official:** https://docs.crewai.com

### Installation

```bash
pip install crewai
pip install crewai-tools
pip install litellm
```

### Our Implementation

This project uses CrewAI version **1.4.1+** with the following stack:
- **LLM Provider:** Google Gemini (via litellm)
- **Model:** gemini-2.5-flash
- **Interface:** GUI (tkinter) + CLI (interactive)

---

## 🧩 Core Components

### 1. Agent

**Purpose:** The autonomous AI worker that performs tasks.

**Import:**
```python
from crewai import Agent
```

**Structure:**
```python
Agent(
    role='string',           # Agent's job title
    goal='string',           # What agent aims to achieve
    backstory='string',      # Agent's background/expertise
    verbose=bool,            # Show thinking process
    allow_delegation=bool,   # Can delegate to other agents
    llm=LLM                  # The AI model to use
)
```

**Parameters Explained:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `role` | str | ✅ Yes | Agent's professional role (e.g., "Research Analyst") |
| `goal` | str | ✅ Yes | What the agent is trying to accomplish |
| `backstory` | str | ✅ Yes | Agent's experience, personality, expertise |
| `verbose` | bool | ❌ No | If True, shows agent's thinking process (default: False) |
| `allow_delegation` | bool | ❌ No | If True, agent can delegate tasks to others (default: True) |
| `llm` | LLM | ✅ Yes | The language model instance |
| `tools` | list | ❌ No | List of tools agent can use |
| `max_iter` | int | ❌ No | Maximum iterations for task (default: 15) |
| `memory` | bool | ❌ No | Enable memory between tasks (default: False) |

**Example from our code:**
```python
researcher = Agent(
    role='Research Analyst',
    goal='Complete the assigned task with high quality',
    backstory="""You are an expert researcher who gathers 
    accurate information and presents it clearly.""",
    verbose=False,
    llm=llm
)
```

---

### 2. Task

**Purpose:** Defines the specific work to be done by an agent.

**Import:**
```python
from crewai import Task
```

**Structure:**
```python
Task(
    description='string',      # Detailed task description
    agent=Agent,              # Which agent does this
    expected_output='string',  # What you expect back
    context=list,             # Dependencies on other tasks
    tools=list                # Tools for this specific task
)
```

**Parameters Explained:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `description` | str | ✅ Yes | Detailed instructions for what needs to be done |
| `agent` | Agent | ✅ Yes | The agent responsible for this task |
| `expected_output` | str | ✅ Yes | Description of the expected result format |
| `context` | list | ❌ No | List of other tasks whose output is needed |
| `tools` | list | ❌ No | Specific tools only for this task |
| `async_execution` | bool | ❌ No | Run task asynchronously (default: False) |
| `output_file` | str | ❌ No | Save output to file |

**Example from our code:**
```python
task = Task(
    description="""Research and explain quantum computing 
    in simple terms with 2 examples.""",
    agent=researcher,
    expected_output="Complete, well-structured response"
)
```

---

### 3. Crew

**Purpose:** Manages and orchestrates agents and tasks.

**Import:**
```python
from crewai import Crew, Process
```

**Structure:**
```python
Crew(
    agents=[Agent, Agent, ...],  # List of agents
    tasks=[Task, Task, ...],      # List of tasks
    verbose=bool,                 # Show execution details
    process=Process               # How to execute tasks
)
```

**Parameters Explained:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `agents` | list | ✅ Yes | List of Agent objects |
| `tasks` | list | ✅ Yes | List of Task objects |
| `verbose` | bool | ❌ No | Show detailed execution logs |
| `process` | Process | ❌ No | Execution order (sequential/hierarchical) |
| `manager_llm` | LLM | ❌ No | LLM for manager in hierarchical process |
| `memory` | bool | ❌ No | Enable crew memory |

**Process Types:**

```python
from crewai import Process

# Sequential: Tasks run one after another
process=Process.sequential

# Hierarchical: Manager agent coordinates
process=Process.hierarchical
```

**Example from our code:**
```python
crew = Crew(
    agents=[researcher],
    tasks=[research_task],
    verbose=False,
    process=Process.sequential
)

# Execute the crew
result = crew.kickoff()
```

---

### 4. LLM (Language Model)

**Purpose:** The AI brain that powers agents.

**Import:**
```python
from crewai import LLM
```

**Structure:**
```python
LLM(
    model='string',        # Model identifier
    temperature=float,     # Creativity level (0-1)
    api_key='string'       # API key for the model
)
```

**Parameters Explained:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `model` | str | ✅ Yes | Model name (e.g., "gemini/gemini-2.5-flash") |
| `temperature` | float | ❌ No | Response creativity (0.0-1.0, default: 0.7) |
| `api_key` | str | ✅ Yes | Authentication key |
| `max_tokens` | int | ❌ No | Maximum response length |
| `timeout` | int | ❌ No | Request timeout in seconds |

**Supported Model Prefixes:**
- `gemini/` - Google Gemini models
- `openai/` - OpenAI models
- `anthropic/` - Anthropic Claude models
- `ollama/` - Local Ollama models

**Example from our code:**
```python
llm = LLM(
    model="gemini/gemini-2.5-flash",
    temperature=0.7,
    api_key=os.getenv("GOOGLE_API_KEY")
)
```

**Temperature Guide:**
- `0.0-0.3` → Focused, consistent, deterministic
- `0.4-0.7` → Balanced (default for most tasks)
- `0.8-1.0` → Creative, varied, experimental

---

## 🔧 Agent Configuration in Detail

### Role Selection

We implement 7 pre-configured roles:

```python
roles = {
    'Research Analyst': {
        'goal': 'Gather and summarize accurate information',
        'backstory': 'Expert at researching and summarizing information'
    },
    'Python Expert': {
        'goal': 'Write clean, efficient Python code',
        'backstory': 'Senior developer who writes clean Python code'
    },
    'Content Writer': {
        'goal': 'Create engaging written content',
        'backstory': 'Skilled at creating engaging written content'
    },
    'Email Writer': {
        'goal': 'Write professional business emails',
        'backstory': 'Professional at writing business emails'
    },
    'Marketing Specialist': {
        'goal': 'Develop marketing strategies',
        'backstory': 'Expert in marketing strategies and campaigns'
    },
    'Data Analyst': {
        'goal': 'Analyze data and provide insights',
        'backstory': 'Analyzes data and provides insights'
    },
    'Creative Writer': {
        'goal': 'Craft compelling narratives',
        'backstory': 'Crafts compelling stories and narratives'
    }
}
```

### Dynamic Agent Creation

**In GUI (`agent_gui.py`):**
```python
def execute_agent(self, task_description):
    # Get selected role
    role = self.role_var.get()
    
    # Backstory mapping
    backstories = {
        "Research Analyst": "You are an expert researcher...",
        # ... other backstories
    }
    
    # Create agent dynamically
    agent = Agent(
        role=role,
        goal='Complete the assigned task with high quality',
        backstory=backstories.get(role, "You are an expert."),
        verbose=False,
        llm=llm
    )
```

**In Interactive (`agent_interactive.py`):**
```python
def get_agent_role():
    # Display role options
    roles = {
        '1': ('Research Analyst', 'Expert at researching...'),
        # ... other roles
    }
    
    # Get user choice
    choice = input("Enter your choice (1-8): ")
    return roles[choice]
```

---

## 📋 Task Configuration in Detail

### Task Description Best Practices

**Good Task Description:**
```python
description="""
Research and explain quantum computing.

Requirements:
1. Simple language (10-year-old level)
2. Include 2 real-world examples
3. Keep under 200 words
4. Use bullet points for key concepts

Format: Introduction, examples, conclusion
"""
```

**Poor Task Description:**
```python
description="Tell me about quantum computing"
```

### Expected Output

**Specific:**
```python
expected_output="200-word explanation with 2 examples in bullet format"
```

**Vague:**
```python
expected_output="Some information"
```

### Task Execution Flow

```
User Input → Task Created → Agent Receives Task → 
LLM Processes → Agent Generates Output → 
Crew Manages → Result Returned
```

---

## 🎯 Crew Management

### Sequential Process (Our Implementation)

```python
crew = Crew(
    agents=[agent1],
    tasks=[task1],
    process=Process.sequential,
    verbose=False
)

# Execute
result = crew.kickoff()
```

**Flow:**
1. Task 1 executes
2. Output goes to next task (if any)
3. Final result returned

### Multi-Agent Sequential

```python
crew = Crew(
    agents=[researcher, writer, editor],
    tasks=[research_task, write_task, edit_task],
    process=Process.sequential
)
```

**Flow:**
1. Researcher completes research_task
2. Writer uses research output for write_task
3. Editor polishes write_task output
4. Final result returned

### Crew Kickoff Methods

**Synchronous (our implementation):**
```python
result = crew.kickoff()  # Blocks until complete
```

**Asynchronous:**
```python
result = await crew.kickoff_async()  # Non-blocking
```

**With Input:**
```python
result = crew.kickoff(inputs={'topic': 'AI'})
```

---

## 🤖 LLM Integration

### Gemini Integration via LiteLLM

**LiteLLM** is a library that provides a unified interface to multiple LLM providers.

**How it works:**
```
CrewAI → LLM class → LiteLLM → Google Gemini API
```

**Configuration:**
```python
from crewai import LLM

llm = LLM(
    model="gemini/gemini-2.5-flash",  # Provider/Model format
    temperature=0.7,
    api_key=os.getenv("GOOGLE_API_KEY")
)
```

### Available Gemini Models

```python
# Fast and free
model="gemini/gemini-2.5-flash"

# More capable
model="gemini/gemini-2.5-pro"

# Always latest
model="gemini/gemini-flash-latest"
model="gemini/gemini-pro-latest"

# Experimental
model="gemini/gemini-2.0-flash-thinking-exp"
```

### Model Selection Logic

**In our code:**
```python
# Default for all agents
llm = LLM(
    model="gemini/gemini-2.5-flash",  # Fast, free, efficient
    temperature=0.7,                   # Balanced creativity
    api_key=api_key
)
```

**Why gemini-2.5-flash?**
- ✅ Fast response times (2-3 seconds)
- ✅ Free tier available
- ✅ Good quality for most tasks
- ✅ Efficient for production use

---

## 🛠️ Tools & Extensions

### CrewAI Tools (Not Used in This Project)

CrewAI supports additional tools that can be added:

```python
from crewai_tools import (
    SerperDevTool,      # Google search
    FileReadTool,       # Read files
    WebsiteSearchTool,  # Search websites
    DirectoryReadTool   # Read directories
)

# Example with tools
agent = Agent(
    role='Researcher',
    tools=[SerperDevTool(), FileReadTool()],
    llm=llm
)
```

**Why we don't use tools:**
- ✅ Simpler setup for beginners
- ✅ No additional API keys needed
- ✅ Gemini's knowledge is sufficient
- ✅ Faster response times

### Custom Tool Creation

**If you want to add tools:**
```python
from crewai_tools import tool

@tool("Calculator")
def calculator(operation: str) -> str:
    """Performs basic math operations"""
    return eval(operation)

# Use in agent
agent = Agent(
    role='Math Expert',
    tools=[calculator],
    llm=llm
)
```

---

## 💻 Code Examples from Our Project

### Example 1: Simple Agent Creation (GUI)

**Location:** `agent_gui.py`, lines 203-217

```python
def execute_agent(self, task_description):
    # Get role from dropdown
    role = self.role_var.get()
    
    # Define backstories
    backstories = {
        "Research Analyst": "You are an expert researcher...",
        # ... more backstories
    }
    
    # Create LLM
    llm = LLM(
        model="gemini/gemini-2.5-flash",
        temperature=0.7,
        api_key=self.api_key
    )
    
    # Create agent
    agent = Agent(
        role=role,
        goal='Complete the assigned task with high quality',
        backstory=backstories.get(role, "Expert in your field"),
        verbose=False,
        llm=llm
    )
    
    # Create task
    task = Task(
        description=task_description,
        agent=agent,
        expected_output="Complete, well-structured response"
    )
    
    # Create and run crew
    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=False
    )
    
    result = crew.kickoff()
    return result
```

### Example 2: Interactive Agent (CLI)

**Location:** `agent_interactive.py`, lines 67-103

```python
def run_agent(role, backstory, task_description, api_key):
    """Execute the agent with given parameters"""
    
    try:
        # Create LLM
        llm = LLM(
            model="gemini/gemini-2.5-flash",
            temperature=0.7,
            api_key=api_key
        )
        
        # Create agent
        agent = Agent(
            role=role,
            goal='Complete the assigned task with high quality',
            backstory=backstory,
            verbose=False,
            llm=llm
        )
        
        # Create task
        task = Task(
            description=task_description,
            agent=agent,
            expected_output="Complete, well-structured response"
        )
        
        # Create and run crew
        crew = Crew(
            agents=[agent],
            tasks=[task],
            verbose=False
        )
        
        result = crew.kickoff()
        
        return True, str(result)
        
    except Exception as e:
        return False, f"Error: {str(e)}"
```

---

## 🔄 Execution Flow Diagram

```
┌─────────────────────────────────────────────────┐
│           USER INTERFACE (GUI/CLI)              │
│  - Select Role                                   │
│  - Enter Task                                    │
│  - Click Run / Press Enter                       │
└─────────────────┬───────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────┐
│         AGENT CONFIGURATION                      │
│  - Role: From user selection                     │
│  - Goal: Pre-defined                            │
│  - Backstory: Mapped from role                  │
│  - LLM: Gemini 2.5 Flash                        │
└─────────────────┬───────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────┐
│           TASK CREATION                          │
│  - Description: User input                       │
│  - Agent: Created agent                          │
│  - Expected Output: "Complete response"          │
└─────────────────┬───────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────┐
│           CREW INITIALIZATION                    │
│  - Agents: [agent]                              │
│  - Tasks: [task]                                │
│  - Process: Sequential                          │
│  - Verbose: False                               │
└─────────────────┬───────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────┐
│              CREW.KICKOFF()                      │
│  - Validates configuration                       │
│  - Starts task execution                         │
│  - Manages agent workflow                        │
└─────────────────┬───────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────┐
│         AGENT PROCESSES TASK                     │
│  1. Receives task description                    │
│  2. Sends to LLM (Gemini API)                   │
│  3. LLM generates response                       │
│  4. Agent formats output                         │
└─────────────────┬───────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────┐
│            RESULT RETURNED                       │
│  - String output from agent                      │
│  - Displayed in GUI/CLI                          │
│  - User can copy/save                            │
└─────────────────────────────────────────────────┘
```

---

## 📊 Configuration Summary

### What We Use

| Component | Value | Reason |
|-----------|-------|--------|
| **CrewAI Version** | 1.4.1+ | Latest stable |
| **LLM Provider** | Google Gemini | Free, fast, quality |
| **Model** | gemini-2.5-flash | Speed + quality balance |
| **Temperature** | 0.7 | Balanced creativity |
| **Process** | Sequential | Simple, predictable |
| **Verbose** | False | Clean UI output |
| **Tools** | None | Simpler setup |
| **Memory** | False | Stateless sessions |

### What We Don't Use (But Could)

- ❌ Multiple agents in parallel
- ❌ Hierarchical process
- ❌ External tools (search, files)
- ❌ Memory between tasks
- ❌ Async execution
- ❌ Custom LLM endpoints

---

## 🚀 Advanced Usage (Not in Current Project)

### Multi-Agent Collaboration

```python
# Create multiple agents
researcher = Agent(role='Researcher', llm=llm)
writer = Agent(role='Writer', llm=llm)
editor = Agent(role='Editor', llm=llm)

# Create sequential tasks
task1 = Task(description="Research topic", agent=researcher)
task2 = Task(description="Write article", agent=writer, context=[task1])
task3 = Task(description="Edit article", agent=editor, context=[task2])

# They work together
crew = Crew(agents=[researcher, writer, editor], tasks=[task1, task2, task3])
```

### With Tools

```python
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

agent = Agent(
    role='Researcher',
    tools=[search_tool],
    llm=llm
)
```

---

## 📖 References

- **CrewAI Docs:** https://docs.crewai.com
- **LiteLLM Docs:** https://docs.litellm.ai
- **Gemini API:** https://ai.google.dev/docs
- **CrewAI GitHub:** https://github.com/joaomdmoura/crewAI

---

## 🎓 Summary

**What CrewAI Does:**
- Creates autonomous AI agents
- Manages tasks and workflows
- Coordinates multiple agents
- Integrates with various LLMs

**What We Implemented:**
- Single-agent system
- 7 pre-configured roles
- Dynamic agent creation
- Gemini AI integration
- Simple, efficient workflow

**Key Takeaway:**
CrewAI provides the structure, Gemini provides the intelligence, and our code provides the interface!

---

**Created for MultiAgent Studio** 🤖
