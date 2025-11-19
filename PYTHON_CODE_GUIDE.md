# 🐍 Python Code Technical Guide

Complete documentation of all Python code, functions, and logic in this project.

---

## 📑 Table of Contents

1. [Project Structure](#project-structure)
2. [Core Python Concepts Used](#core-python-concepts-used)
3. [Agent GUI Code Breakdown](#agent-gui-code-breakdown)
4. [Agent Interactive Code Breakdown](#agent-interactive-code-breakdown)
5. [Functions Reference](#functions-reference)
6. [Error Handling](#error-handling)
7. [Dependencies](#dependencies)

---

## 📁 Project Structure

```
Agent/
├── agent_gui.py              # GUI application (tkinter)
├── agent_interactive.py      # CLI interactive application
├── .env                      # API key storage
├── requirements.txt          # Python dependencies
└── Documentation files
```

---

## 🎯 Core Python Concepts Used

### 1. Object-Oriented Programming (OOP)

**Used in:** `agent_gui.py`

```python
class AgentGUI:
    def __init__(self, root):
        self.root = root
        self.api_key = os.getenv("GOOGLE_API_KEY")
        self.setup_ui()
```

**Why OOP:**
- ✅ Organizes GUI components
- ✅ Maintains state (API key, UI elements)
- ✅ Encapsulates related functions
- ✅ Easier to modify and extend

### 2. Threading

**Used in:** `agent_gui.py`, line 176

```python
thread = threading.Thread(target=self.execute_agent, args=(task_description,))
thread.daemon = True
thread.start()
```

**Why Threading:**
- ✅ Keeps GUI responsive during AI processing
- ✅ Prevents window freezing
- ✅ Shows progress indicator
- ✅ Better user experience

### 3. Environment Variables

**Used in:** Both files

```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
```

**Why Environment Variables:**
- ✅ Secure API key storage
- ✅ Easy configuration
- ✅ Not hardcoded in source
- ✅ Can be changed without editing code

### 4. Exception Handling

**Used in:** Both files

```python
try:
    result = crew.kickoff()
    return True, str(result)
except Exception as e:
    return False, f"Error: {str(e)}"
```

**Why Exception Handling:**
- ✅ Graceful error recovery
- ✅ User-friendly error messages
- ✅ Prevents crashes
- ✅ Helps debugging

### 5. Dictionary Mapping

**Used in:** Both files

```python
backstories = {
    "Research Analyst": "You are an expert researcher...",
    "Python Expert": "You are a senior developer...",
}

backstory = backstories.get(role, "Default backstory")
```

**Why Dictionaries:**
- ✅ Fast lookups
- ✅ Easy to maintain
- ✅ Scalable configuration
- ✅ Clean code structure

---

## 🖥️ Agent GUI Code Breakdown

### File: `agent_gui.py`

**Total Lines:** ~300  
**Language:** Python 3.10+  
**Framework:** tkinter (built-in GUI library)

---

### Class Structure

```python
class AgentGUI:
    def __init__(self, root)          # Initialize GUI
    def setup_ui(self)                # Create UI components
    def clear_placeholder(self, event) # Handle input focus
    def add_placeholder(self, event)   # Add placeholder text
    def clear_output(self)             # Clear result area
    def run_agent(self)                # Start agent execution
    def execute_agent(self, task)      # Run agent in thread
    def display_result(self, result)   # Show success result
    def display_error(self, error)     # Show error message
```

---

### 1. Initialization (`__init__`)

**Lines:** 17-28

```python
def __init__(self, root):
    self.root = root
    self.root.title("🤖 CrewAI Agent - GUI Interface")
    self.root.geometry("900x700")
    self.root.configure(bg='#f0f0f0')
    
    # Check API key
    self.api_key = os.getenv("GOOGLE_API_KEY")
    if not self.api_key:
        messagebox.showerror("Error", "GOOGLE_API_KEY not found in .env file!")
        self.root.destroy()
        return
    
    self.setup_ui()
    self.is_processing = False
```

**What it does:**
1. Stores reference to main window (`root`)
2. Sets window title and size
3. Loads API key from environment
4. Shows error if no API key
5. Calls `setup_ui()` to create interface
6. Initializes `is_processing` flag

**Key Variables:**
- `self.root` → Main window object
- `self.api_key` → Google API key
- `self.is_processing` → Boolean flag to prevent concurrent runs

---

### 2. UI Setup (`setup_ui`)

**Lines:** 30-165

**Structure:**
```python
def setup_ui(self):
    # 1. Title Frame (lines 32-50)
    title_frame = tk.Frame(...)
    title_label = tk.Label(...)
    
    # 2. Main Container (lines 52-54)
    main_frame = tk.Frame(...)
    
    # 3. Role Selection (lines 56-80)
    role_dropdown = ttk.Combobox(...)
    
    # 4. Task Input Box (lines 82-120)
    self.task_input = scrolledtext.ScrolledText(...)
    
    # 5. Buttons (lines 122-145)
    self.run_button = tk.Button(...)
    clear_button = tk.Button(...)
    
    # 6. Progress Bar (lines 147-151)
    self.progress = ttk.Progressbar(...)
    
    # 7. Output Box (lines 153-165)
    self.output_text = scrolledtext.ScrolledText(...)
```

**Key UI Components:**

| Component | Type | Purpose | Variable |
|-----------|------|---------|----------|
| Title | Label | Show app name | `title_label` |
| Role Dropdown | Combobox | Select agent role | `role_var` |
| Task Input | ScrolledText | Enter task description | `task_input` |
| Run Button | Button | Execute agent | `run_button` |
| Clear Button | Button | Reset output | N/A |
| Progress Bar | Progressbar | Show processing | `progress` |
| Status Label | Label | Show current status | `status_label` |
| Output Box | ScrolledText | Display results | `output_text` |

---

### 3. Placeholder Management

**Clear Placeholder (lines 167-170):**
```python
def clear_placeholder(self, event):
    if self.task_input.get('1.0', 'end-1c') == "Example: Explain...":
        self.task_input.delete('1.0', tk.END)
        self.task_input.config(fg='black')
```

**What it does:**
- Triggered when user clicks in input box
- Checks if placeholder text is present
- Removes placeholder
- Changes text color to black

**Add Placeholder (lines 172-176):**
```python
def add_placeholder(self, event):
    if not self.task_input.get('1.0', 'end-1c').strip():
        self.task_input.insert('1.0', "Example: Explain...")
        self.task_input.config(fg='gray')
```

**What it does:**
- Triggered when user clicks away from input box
- Checks if input is empty
- Adds placeholder text back
- Changes text color to gray

---

### 4. Clear Output Function

**Lines:** 178-182

```python
def clear_output(self):
    self.output_text.config(state='normal')
    self.output_text.delete('1.0', tk.END)
    self.output_text.config(state='disabled')
    self.status_label.config(text="Ready", fg='#27ae60')
```

**What it does:**
1. Enable output box editing
2. Delete all content
3. Disable editing again (read-only)
4. Reset status to "Ready"

**Why disable/enable:**
- Output box is read-only for users
- Must enable temporarily to clear
- Re-disable to prevent user editing

---

### 5. Run Agent Function

**Lines:** 184-211

```python
def run_agent(self):
    # 1. Check if already running
    if self.is_processing:
        messagebox.showwarning("Warning", "Agent is already running!")
        return
    
    # 2. Get task text
    task_description = self.task_input.get('1.0', 'end-1c').strip()
    
    # 3. Validate input
    if not task_description or task_description == "Example...":
        messagebox.showwarning("Warning", "Please enter a task!")
        return
    
    # 4. Clear previous output
    self.clear_output()
    
    # 5. Update UI state
    self.is_processing = True
    self.run_button.config(state='disabled', bg='#95a5a6')
    self.status_label.config(text="Agent is working... ⏳", fg='#f39c12')
    self.progress.start(10)
    
    # 6. Run in separate thread
    thread = threading.Thread(target=self.execute_agent, args=(task_description,))
    thread.daemon = True
    thread.start()
```

**Flow:**
```
Check Not Running → Get Input → Validate → 
Clear Output → Update UI → Start Thread
```

**Why threading:**
```python
# Without threading:
result = execute_agent()  # GUI freezes during this!

# With threading:
thread = Thread(target=execute_agent)  # GUI stays responsive!
thread.start()
```

---

### 6. Execute Agent Function

**Lines:** 213-260

```python
def execute_agent(self, task_description):
    try:
        # 1. Get selected role
        role = self.role_var.get()
        
        # 2. Map role to backstory
        backstories = {
            "Research Analyst": "You are an expert researcher...",
            "Python Expert": "You are a senior Python developer...",
            # ... other roles
        }
        
        # 3. Create LLM
        llm = LLM(
            model="gemini/gemini-2.5-flash",
            temperature=0.7,
            api_key=self.api_key
        )
        
        # 4. Create agent
        agent = Agent(
            role=role,
            goal='Complete the assigned task with high quality',
            backstory=backstories.get(role, "You are an expert."),
            verbose=False,
            llm=llm
        )
        
        # 5. Create task
        task = Task(
            description=task_description,
            agent=agent,
            expected_output="Complete, well-structured response"
        )
        
        # 6. Create and run crew
        crew = Crew(
            agents=[agent],
            tasks=[task],
            verbose=False
        )
        
        result = crew.kickoff()
        
        # 7. Display result (thread-safe)
        self.root.after(0, self.display_result, str(result))
        
    except Exception as e:
        error_msg = f"Error: {str(e)}"
        self.root.after(0, self.display_error, error_msg)
```

**Thread Safety:**
```python
# Wrong (not thread-safe):
self.display_result(result)

# Correct (thread-safe):
self.root.after(0, self.display_result, result)
```

`root.after(0, ...)` schedules GUI updates on the main thread.

---

### 7. Display Functions

**Display Result (lines 262-270):**
```python
def display_result(self, result):
    self.output_text.config(state='normal')
    self.output_text.insert('1.0', result)
    self.output_text.config(state='disabled')
    
    self.is_processing = False
    self.run_button.config(state='normal', bg='#27ae60')
    self.status_label.config(text="✅ Complete!", fg='#27ae60')
    self.progress.stop()
```

**Display Error (lines 272-283):**
```python
def display_error(self, error_msg):
    self.output_text.config(state='normal')
    self.output_text.insert('1.0', error_msg)
    self.output_text.config(state='disabled')
    
    self.is_processing = False
    self.run_button.config(state='normal', bg='#27ae60')
    self.status_label.config(text="❌ Error", fg='#e74c3c')
    self.progress.stop()
    
    messagebox.showerror("Error", "Failed to run agent.")
```

---

### Main Execution Block

**Lines:** 286-289

```python
if __name__ == "__main__":
    root = tk.Tk()
    app = AgentGUI(root)
    root.mainloop()
```

**What it does:**
1. `tk.Tk()` → Create main window
2. `AgentGUI(root)` → Initialize our application
3. `root.mainloop()` → Start GUI event loop (wait for user interaction)

---

## 💻 Agent Interactive Code Breakdown

### File: `agent_interactive.py`

**Total Lines:** ~170  
**Language:** Python 3.10+  
**Type:** Command-line interface

---

### Function Structure

```python
def print_header()              # Display welcome banner
def get_agent_role()            # Let user select role
def get_task_input()            # Get multi-line task input
def run_agent(...)              # Execute CrewAI agent
def display_result(...)         # Show formatted result
def main()                      # Main program loop
```

---

### 1. Print Header Function

**Lines:** 10-15

```python
def print_header():
    """Display welcome header"""
    print("\n" + "=" * 70)
    print("🤖 INTERACTIVE AI AGENT")
    print("Powered by Google Gemini AI")
    print("=" * 70)
    print()
```

**What it does:**
- Displays application title
- Shows branding
- Creates visual separator

**Output:**
```
======================================================================
🤖 INTERACTIVE AI AGENT
Powered by Google Gemini AI
======================================================================
```

---

### 2. Get Agent Role Function

**Lines:** 17-44

```python
def get_agent_role():
    """Let user select agent role"""
    print("📋 SELECT AGENT ROLE:")
    print()
    
    roles = {
        '1': ('Research Analyst', 'Expert at researching...'),
        '2': ('Python Expert', 'Senior developer...'),
        '3': ('Content Writer', 'Skilled at creating...'),
        '4': ('Email Writer', 'Professional at writing...'),
        '5': ('Marketing Specialist', 'Expert in marketing...'),
        '6': ('Data Analyst', 'Analyzes data...'),
        '7': ('Creative Writer', 'Crafts compelling...'),
        '8': ('Custom', 'Define your own agent role')
    }
    
    # Display options
    for key, (role, desc) in roles.items():
        print(f"  {key}. {role:<20} - {desc}")
    
    print()
    choice = input("Enter your choice (1-8): ").strip()
    
    # Handle custom role
    if choice in roles:
        if choice == '8':
            role = input("Enter custom role name: ").strip()
            backstory = input("Enter agent expertise/background: ").strip()
        else:
            role, backstory = roles[choice]
        return role, backstory
    else:
        print("⚠️  Invalid choice. Using default 'Research Analyst'")
        return roles['1']
```

**Flow:**
```
Display Menu → Get User Input → 
If Custom → Get Custom Details → Return Role & Backstory
```

**Why tuples:**
```python
roles = {
    '1': ('Research Analyst', 'Expert at...')  # Tuple: immutable pair
}
```
Tuples are perfect for fixed pairs of data.

---

### 3. Get Task Input Function

**Lines:** 46-64

```python
def get_task_input():
    """Get task description from user"""
    print("\n" + "-" * 70)
    print("📝 WHAT DO YOU WANT THE AGENT TO DO?")
    print("-" * 70)
    print()
    print("Examples:")
    print("  • Explain quantum computing in simple terms")
    print("  • Write a Python function to calculate fibonacci numbers")
    print("  • Create a professional email thanking a client")
    print("  • Research the benefits of meditation")
    print()
    print("Your task (press Enter twice when done):")
    print()
    
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            if lines:
                break
    
    return ' '.join(lines)
```

**Multi-line Input Logic:**
```python
lines = []
while True:
    line = input()
    if line:
        lines.append(line)  # Add non-empty lines
    else:
        if lines:
            break  # Empty line + has content = done
```

**Example:**
```
User types: "Write a function"
User presses Enter
User types: "to calculate prime numbers"
User presses Enter
User presses Enter again (empty line)
→ Result: "Write a function to calculate prime numbers"
```

---

### 4. Run Agent Function

**Lines:** 66-105

```python
def run_agent(role, backstory, task_description, api_key):
    """Execute the agent with given parameters"""
    print("\n" + "=" * 70)
    print("⏳ AGENT IS WORKING...")
    print("=" * 70)
    print()
    
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

**Return Pattern:**
```python
return success (bool), result (str)

# Success case:
return True, "Agent's response here..."

# Error case:
return False, "Error: Something went wrong"
```

This pattern allows the caller to handle both cases easily.

---

### 5. Display Result Function

**Lines:** 107-118

```python
def display_result(success, result):
    """Display the agent's response"""
    print("\n" + "=" * 70)
    if success:
        print("✅ AGENT RESPONSE:")
    else:
        print("❌ ERROR:")
    print("=" * 70)
    print()
    print(result)
    print()
    print("=" * 70)
```

**Conditional Formatting:**
```python
if success:
    print("✅ AGENT RESPONSE:")  # Green checkmark
else:
    print("❌ ERROR:")           # Red X
```

---

### 6. Main Function

**Lines:** 120-163

```python
def main():
    """Main program loop"""
    # Check API key
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        print("\n❌ ERROR: GOOGLE_API_KEY not found!")
        print("\nPlease make sure .env file exists with your API key.")
        return
    
    print_header()
    
    while True:
        # Get agent role
        role, backstory = get_agent_role()
        
        # Get task
        task_description = get_task_input()
        
        if not task_description.strip():
            print("\n⚠️  No task entered. Please try again.")
            continue
        
        # Run agent
        success, result = run_agent(role, backstory, task_description, api_key)
        
        # Display result
        display_result(success, result)
        
        # Ask to continue
        print("\n" + "-" * 70)
        continue_choice = input("Do you want to run another task? (yes/no): ").strip().lower()
        
        if continue_choice not in ['yes', 'y']:
            print("\n👋 Thank you for using the AI Agent! Goodbye!")
            print("=" * 70)
            break
        
        print("\n\n")
```

**Program Flow:**
```
Check API Key → Print Header → 
LOOP:
  Get Role → Get Task → Run Agent → Display Result → 
  Ask Continue? → If No, Exit
```

---

### Main Execution Block

**Lines:** 165-170

```python
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
```

**Exception Handling:**
- `KeyboardInterrupt` → User pressed Ctrl+C
- `Exception` → Catch-all for unexpected errors

---

## 🔧 Functions Reference

### GUI Functions Summary

| Function | Purpose | Returns | Thread-Safe |
|----------|---------|---------|-------------|
| `__init__(root)` | Initialize GUI | None | N/A |
| `setup_ui()` | Create UI elements | None | ✅ Yes |
| `clear_placeholder(event)` | Remove placeholder text | None | ✅ Yes |
| `add_placeholder(event)` | Add placeholder text | None | ✅ Yes |
| `clear_output()` | Clear output box | None | ✅ Yes |
| `run_agent()` | Start agent execution | None | ✅ Yes |
| `execute_agent(task)` | Run agent (threaded) | None | ❌ No (runs in thread) |
| `display_result(result)` | Show success | None | ✅ Yes |
| `display_error(error)` | Show error | None | ✅ Yes |

### Interactive Functions Summary

| Function | Purpose | Parameters | Returns |
|----------|---------|------------|---------|
| `print_header()` | Display banner | None | None |
| `get_agent_role()` | Get role choice | None | (role, backstory) |
| `get_task_input()` | Get multi-line task | None | task_string |
| `run_agent(...)` | Execute agent | role, backstory, task, key | (success, result) |
| `display_result(...)` | Show result | success, result | None |
| `main()` | Main program loop | None | None |

---

## ⚠️ Error Handling

### GUI Error Handling

**1. Missing API Key:**
```python
if not self.api_key:
    messagebox.showerror("Error", "GOOGLE_API_KEY not found!")
    self.root.destroy()  # Close window
    return
```

**2. Empty Task Input:**
```python
if not task_description or task_description == "Example...":
    messagebox.showwarning("Warning", "Please enter a task!")
    return
```

**3. Agent Execution Error:**
```python
try:
    result = crew.kickoff()
except Exception as e:
    self.root.after(0, self.display_error, str(e))
```

### Interactive Error Handling

**1. Missing API Key:**
```python
if not api_key:
    print("\n❌ ERROR: GOOGLE_API_KEY not found!")
    return
```

**2. Empty Task:**
```python
if not task_description.strip():
    print("\n⚠️  No task entered. Please try again.")
    continue
```

**3. Agent Error:**
```python
try:
    result = crew.kickoff()
    return True, str(result)
except Exception as e:
    return False, f"Error: {str(e)}"
```

**4. Keyboard Interrupt:**
```python
except KeyboardInterrupt:
    print("\n\n👋 Interrupted by user. Goodbye!")
```

---

## 📦 Dependencies

### requirements.txt

```txt
crewai>=1.4.1
crewai-tools>=1.4.1
litellm>=1.79.0
python-dotenv>=1.0.0
```

### Import Statements

**agent_gui.py:**
```python
import tkinter as tk                    # GUI framework
from tkinter import scrolledtext        # Scrollable text widget
from tkinter import messagebox          # Popup messages
from tkinter import ttk                 # Themed widgets
from crewai import Agent, Task, Crew, LLM  # AI framework
import os                               # Environment variables
from dotenv import load_dotenv          # Load .env files
import threading                        # Multi-threading
```

**agent_interactive.py:**
```python
from crewai import Agent, Task, Crew, LLM  # AI framework
import os                               # Environment variables
from dotenv import load_dotenv          # Load .env files
```

---

## 🎓 Key Python Patterns Used

### 1. Class-Based GUI (OOP)
```python
class AgentGUI:
    def __init__(self):
        # Initialize
    
    def method(self):
        # Access with self.
```

### 2. Function-Based CLI
```python
def function1():
    # Do something

def function2():
    # Do something else

def main():
    function1()
    function2()
```

### 3. Thread-Safe GUI Updates
```python
# Schedule on main thread
self.root.after(0, self.update_function, data)
```

### 4. Error Recovery Pattern
```python
try:
    risky_operation()
    return True, result
except Exception as e:
    return False, error_message
```

### 5. Environment Configuration
```python
load_dotenv()
value = os.getenv("KEY_NAME", "default")
```

---

## 📊 Code Statistics

### agent_gui.py
- **Lines:** ~300
- **Functions:** 9
- **Classes:** 1
- **Threading:** Yes
- **Complexity:** Medium-High

### agent_interactive.py
- **Lines:** ~170
- **Functions:** 6
- **Classes:** 0
- **Threading:** No
- **Complexity:** Low-Medium

---

## 🚀 Performance Considerations

### GUI Version
- ✅ Threading prevents UI freezing
- ✅ Daemon threads auto-cleanup
- ⚠️ More memory usage (~50MB)
- ⚠️ Tkinter startup overhead

### Interactive Version
- ✅ Lightweight (~10MB memory)
- ✅ Fast startup
- ⚠️ Blocks during execution
- ✅ Lower CPU usage

---

## 📖 Summary

**What the Python code does:**
1. Loads API key from `.env`
2. Creates user interface (GUI or CLI)
3. Accepts user input (role + task)
4. Configures CrewAI agent
5. Executes agent via Gemini AI
6. Displays formatted results
7. Handles errors gracefully

**Key techniques:**
- Object-oriented design (GUI)
- Functional design (Interactive)
- Multi-threading (GUI responsiveness)
- Environment variables (security)
- Exception handling (reliability)
- Dictionary mapping (configuration)

---

**Created for MultiAgent Studio** 🐍
