# 🎨 How to Use the GUI and Interactive Versions

## 📁 New Files Created

1. **`agent_gui.py`** - Beautiful graphical interface
2. **`agent_interactive.py`** - Command-line interactive version

---

## 🖥️ Option 1: GUI Version (Recommended for Beginners)

### Features:
- ✅ Beautiful graphical interface
- ✅ Select agent role from dropdown
- ✅ Type your task in text box
- ✅ Click button to run
- ✅ See results in real-time
- ✅ Progress indicator
- ✅ No commands needed!

### How to Run:

```powershell
python agent_gui.py
```

### How to Use:

1. **Window opens automatically**
2. **Select agent role** from dropdown:
   - Research Analyst
   - Python Expert
   - Content Writer
   - Email Writer
   - Marketing Specialist
   - Data Analyst
   - Creative Writer

3. **Type your task** in the text box
   - Example: "Explain blockchain in simple terms"

4. **Click 🚀 Run Agent** button

5. **Wait** - progress bar shows it's working

6. **See results** in the response box below

### Screenshot Guide:

```
┌────────────────────────────────────────┐
│  🤖 AI Agent Assistant                 │
│  Powered by Google Gemini AI           │
├────────────────────────────────────────┤
│                                        │
│ 1️⃣ Select Agent Role                   │
│ [Research Analyst ▼]                   │
│                                        │
│ 2️⃣ What do you want agent to do?       │
│ ┌────────────────────────────────────┐ │
│ │ Your task here...                  │ │
│ │                                    │ │
│ └────────────────────────────────────┘ │
│                                        │
│ [🚀 Run Agent] [🗑️ Clear] [Progress]   │
│                                        │
│ 3️⃣ Agent Response                       │
│ ┌────────────────────────────────────┐ │
│ │ Results appear here...             │ │
│ │                                    │ │
│ └────────────────────────────────────┘ │
└────────────────────────────────────────┘
```

---

## 💻 Option 2: Interactive Command-Line Version

### Features:
- ✅ Interactive Q&A style
- ✅ Choose role each time
- ✅ Multi-line input support
- ✅ Run multiple tasks in sequence
- ✅ Custom roles supported
- ✅ Works in any terminal

### How to Run:

```powershell
python agent_interactive.py
```

### How to Use:

1. **Program starts** - shows welcome message

2. **Select agent role** - Type number 1-8:
   ```
   1. Research Analyst
   2. Python Expert
   3. Content Writer
   4. Email Writer
   5. Marketing Specialist
   6. Data Analyst
   7. Creative Writer
   8. Custom (define your own)
   ```

3. **Enter your task**:
   - Type your task
   - Can use multiple lines
   - Press Enter twice when done

4. **Wait** - Agent processes your request

5. **See results** - Response displays

6. **Continue?** - Choose to run another task or exit

### Example Session:

```
======================================================================
🤖 INTERACTIVE AI AGENT
Powered by Google Gemini AI
======================================================================

📋 SELECT AGENT ROLE:

  1. Research Analyst      - Expert at researching and summarizing information
  2. Python Expert         - Senior developer who writes clean Python code
  3. Content Writer        - Skilled at creating engaging written content
  ...

Enter your choice (1-8): 1

----------------------------------------------------------------------
📝 WHAT DO YOU WANT THE AGENT TO DO?
----------------------------------------------------------------------

Your task (press Enter twice when done):

Explain what quantum computing is in simple terms with 2 examples
[Press Enter]
[Press Enter again]

======================================================================
⏳ AGENT IS WORKING...
======================================================================

======================================================================
✅ AGENT RESPONSE:
======================================================================

[Response appears here...]

----------------------------------------------------------------------
Do you want to run another task? (yes/no): 
```

---

## 🆚 Which One Should You Use?

### Use GUI (`agent_gui.py`) if you:
- ✅ Prefer clicking over typing
- ✅ Want a visual interface
- ✅ Are new to command line
- ✅ Want to see everything at once
- ✅ Like modern applications

### Use Interactive (`agent_interactive.py`) if you:
- ✅ Prefer keyboard over mouse
- ✅ Work mostly in terminal
- ✅ Want quick access
- ✅ Need to run multiple tasks quickly
- ✅ Like command-line tools

---

## 🎯 Quick Comparison

| Feature | GUI | Interactive |
|---------|-----|-------------|
| **Interface** | Graphical window | Command line |
| **Ease of use** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Speed** | Click button | Type commands |
| **Multi-line input** | ✅ Easy | ✅ Supported |
| **Visual feedback** | Progress bar | Text messages |
| **Copy results** | ✅ Easy | ✅ Easy |
| **Resource usage** | Higher | Lower |

---

## 💡 Tips & Tricks

### For GUI:
- **Copy results**: Select text in response box and Ctrl+C
- **Clear quickly**: Click 🗑️ Clear button
- **While running**: Progress bar shows it's working
- **Multiple tasks**: Just change task and click Run again

### For Interactive:
- **Multi-line tasks**: Press Enter twice when done typing
- **Quick exit**: Answer 'no' when asked to continue
- **Force quit**: Press Ctrl+C anytime
- **Custom roles**: Choose option 8 to define your own

---

## 🔧 Customization

### Change Available Roles (GUI)

Edit `agent_gui.py` line ~82:

```python
roles = [
    "Research Analyst",
    "Python Expert",
    "Your Custom Role",  # Add here!
    # ...
]
```

And add backstory at line ~139:

```python
backstories = {
    # ...
    "Your Custom Role": "Description of your role",
}
```

### Change Model Speed

In both files, find this line:

```python
model="gemini/gemini-2.5-flash",  # Fast
```

Change to:
```python
model="gemini/gemini-2.5-pro",  # More capable but slower
```

---

## 🐛 Troubleshooting

### GUI doesn't open
**Problem:** Window doesn't appear  
**Solution:** Make sure tkinter is installed (comes with Python by default)

### "API key not found"
**Problem:** Error about missing API key  
**Solution:** Check `.env` file exists with your API key

### GUI freezes
**Problem:** Window becomes unresponsive  
**Solution:** This is normal while agent is working. Wait for completion.

### Interactive won't accept input
**Problem:** Can't type in interactive mode  
**Solution:** Make sure to press Enter twice to submit multi-line input

---

## 🎨 Examples to Try

### Research Tasks:
```
Explain climate change in 150 words with 3 key points
```

### Coding Tasks:
```
Write a Python function to check if a string is a palindrome
```

### Writing Tasks:
```
Write a professional email requesting a project deadline extension
```

### Creative Tasks:
```
Create 3 taglines for a coffee shop targeting students
```

---

## 🚀 Next Steps

1. **Try the GUI first** - easiest to get started
2. **Experiment with different roles** - see what works best
3. **Try the interactive version** - for faster workflows
4. **Customize roles** - add your own agent types
5. **Share results** - copy and use the outputs!

---

## 📝 Summary

**GUI Version:**
```powershell
python agent_gui.py
```
→ Click, type, run - that's it!

**Interactive Version:**
```powershell
python agent_interactive.py
```
→ Choose role, enter task, get results!

Both versions:
- ✅ Use your `.env` API key automatically
- ✅ Support all agent roles
- ✅ Work with any task
- ✅ Easy to use
- ✅ Professional results

**Have fun creating with AI!** 🎉
