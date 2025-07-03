#!/usr/bin/env python3
"""
Setup and run script for AI Trading Dashboard
This script helps you install dependencies and run the applications
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("🔧 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully!")
    except subprocess.CalledProcessError:
        print("❌ Error installing dependencies. Please check your internet connection.")
        return False
    return True

def run_dashboard():
    """Run the main dashboard"""
    print("🚀 Starting AI Trading Dashboard...")
    print("📖 The dashboard will open in your browser at http://localhost:8501")
    print("💡 Use the sidebar to enter ticker symbols and get AI recommendations!")
    
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "streamlit_dashboard.py"])
    except KeyboardInterrupt:
        print("\n👋 Dashboard stopped.")

def run_chatbot():
    """Run the chatbot interface"""
    print("🤖 Starting AI Trading Chatbot...")
    print("📖 The chatbot will open in your browser at http://localhost:8501")
    print("💬 Just type ticker symbols like 'AAPL' or 'What about GOOGL?' for analysis!")
    
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "chatbot_interface.py"])
    except KeyboardInterrupt:
        print("\n👋 Chatbot stopped.")

def main():
    print("""
🤖 AI Trading Agent Setup
========================

This tool will help you set up and run your AI trading dashboard.

Available options:
1. Install dependencies
2. Run dashboard interface (comprehensive analysis)
3. Run chatbot interface (conversational)
4. Exit
""")

    while True:
        try:
            choice = input("\nEnter your choice (1-4): ").strip()
            
            if choice == "1":
                if install_requirements():
                    print("\n✨ Ready to run! Choose option 2 or 3 to start the interface.")
                    
            elif choice == "2":
                if not os.path.exists("requirements.txt"):
                    print("❌ requirements.txt not found. Please run option 1 first.")
                    continue
                run_dashboard()
                
            elif choice == "3":
                if not os.path.exists("requirements.txt"):
                    print("❌ requirements.txt not found. Please run option 1 first.")
                    continue
                run_chatbot()
                
            elif choice == "4":
                print("👋 Goodbye!")
                break
                
            else:
                print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")
                
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main() 