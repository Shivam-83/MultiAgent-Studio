"""
MultiAgent Studio - Streamlit Web Interface
A modern web UI to interact with your multi-role AI agent.

Run with:
    streamlit run agent_streamlit.py
"""

import os

import streamlit as st
from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    # We don't stop execution here because Streamlit reruns the script.
    # We'll show an error in the UI instead.
    pass

# ----- App Config -----
APP_TITLE = "MultiAgent Studio"
APP_TAGLINE = "Multi-role AI assistant powered by CrewAI & Google Gemini"

st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🤖",
    layout="wide",
)

# ----- Helper: Role Config -----
ROLE_CONFIG = {
    "Research Analyst": {
        "goal": "Gather and summarize accurate information",
        "backstory": "You are an expert researcher who gathers accurate information and presents it clearly.",
    },
    "Python Expert": {
        "goal": "Write clean, efficient, well-documented Python code",
        "backstory": "You are a senior Python developer who writes production-quality code and explains it clearly.",
    },
    "Content Writer": {
        "goal": "Create engaging, well-structured content",
        "backstory": "You are a skilled content writer who makes complex topics easy to understand.",
    },
    "Email Writer": {
        "goal": "Write clear, professional emails",
        "backstory": "You are a professional communication specialist who writes effective business emails.",
    },
    "Marketing Specialist": {
        "goal": "Develop practical, creative marketing ideas",
        "backstory": "You are a creative marketer who designs campaigns that convert.",
    },
    "Data Analyst": {
        "goal": "Analyze data and provide actionable insights",
        "backstory": "You are a data analyst who explains numbers in plain language and focuses on decisions.",
    },
    "Creative Writer": {
        "goal": "Craft compelling stories and narratives",
        "backstory": "You are a creative storyteller who writes vivid, memorable content.",
    },
}

ROLE_LIST = list(ROLE_CONFIG.keys())

# ----- Helper: Run Agent -----

def run_agent(role: str, task_description: str, api_key: str) -> tuple[bool, str]:
    """Run a CrewAI agent for the given role and task.

    Returns (success: bool, message: str).
    """
    try:
        role_info = ROLE_CONFIG.get(role, {})
        goal = role_info.get("goal", "Complete the assigned task with high quality and clarity")
        backstory = role_info.get("backstory", "You are an expert in your field and communicate clearly.")

        # Create LLM
        llm = LLM(
            model="gemini/gemini-2.5-flash",
            temperature=0.7,
            api_key=api_key,
        )

        # Create agent
        agent = Agent(
            role=role,
            goal=goal,
            backstory=backstory,
            verbose=False,
            llm=llm,
        )

        # Create task
        task = Task(
            description=task_description,
            agent=agent,
            expected_output="Complete, well-structured response",
        )

        # Create and run crew
        crew = Crew(
            agents=[agent],
            tasks=[task],
            verbose=False,
        )

        result = crew.kickoff()
        return True, str(result)

    except Exception as e:
        return False, f"Error while running agent: {e}"


# ----- UI -----

st.title("🤖 " + APP_TITLE)
st.caption(APP_TAGLINE)

# Sidebar: settings
with st.sidebar:
    st.header("⚙️ Settings")

    if not API_KEY:
        st.error(
            "`GOOGLE_API_KEY` not found. Set it in your `.env` file or environment variables before using the app.",
        )
    else:
        st.success("API key loaded successfully.")

    st.markdown("---")
    st.subheader("Agent Configuration")

    selected_role = st.selectbox("Agent role", ROLE_LIST, index=0)

    temperature = st.slider(
        "Creativity (temperature)",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1,
        help="Lower = more focused, higher = more creative.",
    )

    # Model selector (for future expansion)
    model_choice = st.selectbox(
        "Model", ["gemini/gemini-2.5-flash", "gemini/gemini-2.5-pro"], index=0
    )

# Main layout
col_input, col_output = st.columns([1, 1])

with col_input:
    st.subheader("📝 Task")

    example_prompt = (
        "Example: Explain artificial intelligence in simple terms with 3 real-world examples, "
        "or ask the Python Expert to write a function, or ask the Email Writer to draft a message."
    )

    task_text = st.text_area(
        "What do you want the agent to do?",
        height=220,
        placeholder=example_prompt,
    )

    run_clicked = st.button("🚀 Run Agent", type="primary")

with col_output:
    st.subheader("📤 Agent Response")

    if "last_result" not in st.session_state:
        st.session_state.last_result = ""

    if st.session_state.last_result:
        st.markdown(st.session_state.last_result)

# Handle run
if run_clicked:
    if not API_KEY:
        st.error("`GOOGLE_API_KEY` is not set. Please configure your API key and refresh the page.")
    elif not task_text.strip():
        st.warning("Please enter a task description before running the agent.")
    else:
        with st.spinner("Agent is working... this may take a few seconds"):
            # Override model and temperature dynamically
            # (We recreate LLM inside run_agent, so pass via globals)
            # Easiest: temporarily patch ROLE_CONFIG if needed, but here we only adjust temperature/model via LLM.

            # Create a custom runner that passes dynamic model/temperature
            try:
                llm = LLM(
                    model=model_choice,
                    temperature=temperature,
                    api_key=API_KEY,
                )

                role_info = ROLE_CONFIG.get(selected_role, {})
                goal = role_info.get("goal", "Complete the assigned task with high quality and clarity")
                backstory = role_info.get("backstory", "You are an expert in your field and communicate clearly.")

                agent = Agent(
                    role=selected_role,
                    goal=goal,
                    backstory=backstory,
                    verbose=False,
                    llm=llm,
                )

                task = Task(
                    description=task_text,
                    agent=agent,
                    expected_output="Complete, well-structured response",
                )

                crew = Crew(
                    agents=[agent],
                    tasks=[task],
                    verbose=False,
                )

                success = True
                result = crew.kickoff()
                result_text = str(result)

            except Exception as e:
                success = False
                result_text = f"Error while running agent: {e}"

        # Display result
        if success:
            st.success("Agent completed the task.")
            st.session_state.last_result = result_text
            st.markdown("### 📄 Response")
            st.markdown(result_text)
        else:
            st.error("The agent failed to run.")
            st.code(result_text, language="text")
