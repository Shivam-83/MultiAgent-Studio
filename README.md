# 🤖 MultiAgent Studio

Multi-role AI assistant with a Streamlit web UI and an interactive CLI, powered by CrewAI & Google Gemini.

## 📁 What's Inside

- **`agent_streamlit.py`** - Streamlit web interface (main UI)
- **`agent_interactive.py`** - Interactive command-line version
- **`.env`** - Your API key (already configured)
- **`requirements.txt`** - Required packages

---

## 🚀 Quick Start

### Option 1: Streamlit Web App (Recommended)

```powershell
streamlit run agent_streamlit.py
```

**Features:**
- ✅ Clean, modern web interface
- ✅ 7 pre-configured agent roles
- ✅ Works in your browser
- ✅ No HTML/JS required

**How to use:**
1. Run the above command
2. Your browser will open automatically
3. Select an agent role from the sidebar
4. Type your task in the text area
5. Click "🚀 Run Agent"
6. Read and copy the response

---

### Option 2: Interactive CLI

```powershell
python agent_interactive.py
```

**Features:**
- ✅ Fast keyboard-based interface
- ✅ Multi-line input support
- ✅ Run multiple tasks in sequence
- ✅ Custom role support

**How to use:**
1. Choose agent role (1-8)
2. Type your task (press Enter twice)
3. See results!
4. Continue or exit

---

## 🎯 Available Agent Roles

Both versions include:

1. **Research Analyst** - Researches and summarizes topics
2. **Python Expert** - Writes Python code with documentation
3. **Content Writer** - Creates engaging articles
4. **Email Writer** - Writes professional emails
5. **Marketing Specialist** - Develops marketing strategies
6. **Data Analyst** - Analyzes data and provides insights
7. **Creative Writer** - Crafts stories and narratives

---

## 💡 Example Tasks

**Research:**
```
Explain quantum computing in simple terms with 2 examples
```

**Coding:**
```
Write a Python function to check if a number is prime
```

**Writing:**
```
Create a professional thank you email for a client
```

**Creative:**
```
Write 5 taglines for a coffee shop targeting students
```

---

## ⚙️ Setup (Already Done!)

Your API key is stored in `.env` file and automatically loads when you run the agents.

**If you need to change it:**

Edit `.env` file:
```
GOOGLE_API_KEY=your-new-api-key-here
```

---

## 📚 Documentation

- **`HOW_TO_USE_GUI.md`** - Complete guide for both versions
- **`BEGINNER_GUIDE.md`** - Learn to create agents from scratch

---

## 🔧 Requirements

```bash
pip install crewai crewai-tools litellm google-generativeai python-dotenv
```

*(Already installed if you've been using the agents)*

---

## 🐛 Troubleshooting

**"API key not found" error:**
- Check `.env` file exists
- Verify it contains: `GOOGLE_API_KEY=your-key`

**Streamlit app doesn't open in browser:**
- After running `streamlit run agent_streamlit.py`, copy the `Local URL` shown in the terminal into your browser.

**Agent takes too long:**
- Normal for first run
- Subsequent runs are faster
- Check internet connection

---

## 🎨 Which Version to Use?

**Use GUI if you:**
- Prefer clicking over typing
- Want visual feedback
- Are new to command line
- Like modern applications

**Use Interactive if you:**
- Prefer keyboard over mouse
- Work mostly in terminal
- Want quick access
- Like command-line tools

---

## 🎉 You're Ready!

Just run the Streamlit app:
```powershell
streamlit run agent_streamlit.py
```

Or use the CLI:

```powershell
python agent_interactive.py
```

**No setup needed - everything is configured!** ✨

---

## 📖 Learn More

- **Gemini API**: https://ai.google.dev/docs
- **CrewAI Docs**: https://docs.crewai.com
- **Get API Key**: https://makersuite.google.com/app/apikey

---

**Made with ❤️ using CrewAI and Google Gemini AI**
