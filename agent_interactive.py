"""
Interactive CrewAI Agent - Command Line Version
Takes user input and generates responses
"""

from crewai import Agent, Task, Crew, LLM
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()

def print_header():
    """Display welcome header"""
    print("\n" + "=" * 70)
    print("🤖 MultiAgent Studio - CLI")
    print("Multi-role AI assistant powered by CrewAI & Google Gemini")
    print("=" * 70)
    print()

def get_agent_role():
    """Let user select agent role"""
    print("📋 SELECT AGENT ROLE:")
    print()
    
    roles = {
        '1': ('Research Analyst', 'Expert at researching and summarizing information'),
        '2': ('Python Expert', 'Senior developer who writes clean Python code'),
        '3': ('Content Writer', 'Skilled at creating engaging written content'),
        '4': ('Email Writer', 'Professional at writing business emails'),
        '5': ('Marketing Specialist', 'Expert in marketing strategies and campaigns'),
        '6': ('Data Analyst', 'Analyzes data and provides insights'),
        '7': ('Creative Writer', 'Crafts compelling stories and narratives'),
        '8': ('Custom', 'Define your own agent role')
    }
    
    for key, (role, desc) in roles.items():
        print(f"  {key}. {role:<20} - {desc}")
    
    print()
    choice = input("Enter your choice (1-8): ").strip()
    
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

def main():
    """Main program loop"""
    # Check API key
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        print("\n❌ ERROR: GOOGLE_API_KEY not found!")
        print("\nPlease make sure .env file exists with your API key.")
        print("Or set it manually: $env:GOOGLE_API_KEY='your-key'")
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

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
