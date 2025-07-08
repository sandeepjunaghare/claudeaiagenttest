#!/usr/bin/env python3
"""
AI Agent - A simple interactive AI assistant
"""

import sys
import json
from datetime import datetime

class AIAgent:
    def __init__(self):
        self.name = "AI Agent"
        self.version = "1.0.0"
        self.commands = {
            "help": self.show_help,
            "time": self.get_time,
            "echo": self.echo_message,
            "calculate": self.calculate,
            "quit": self.quit_agent,
            "exit": self.quit_agent
        }
    
    def show_help(self, args=None):
        """Display available commands"""
        print(f"\n{self.name} v{self.version} - Available commands:")
        print("  help - Show this help message")
        print("  time - Display current time")
        print("  echo <message> - Echo back your message")
        print("  calculate <expression> - Calculate a math expression")
        print("  quit/exit - Exit the agent")
        print()
    
    def get_time(self, args=None):
        """Get current time"""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Current time: {current_time}")
    
    def echo_message(self, args):
        """Echo back user message"""
        if args:
            message = " ".join(args)
            print(f"Echo: {message}")
        else:
            print("Error: No message provided to echo")
    
    def calculate(self, args):
        """Calculate a simple math expression"""
        if not args:
            print("Error: No expression provided")
            return
        
        try:
            expression = " ".join(args)
            # Only allow basic math operations for security
            allowed_chars = set("0123456789+-*/.() ")
            if not all(c in allowed_chars for c in expression):
                print("Error: Invalid characters in expression")
                return
            
            result = eval(expression)
            print(f"Result: {expression} = {result}")
        except Exception as e:
            print(f"Error calculating expression: {e}")
    
    def quit_agent(self, args=None):
        """Exit the agent"""
        print("Goodbye!")
        sys.exit(0)
    
    def process_command(self, command_line):
        """Process a user command"""
        if not command_line.strip():
            return
        
        parts = command_line.strip().split()
        command = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else []
        
        if command in self.commands:
            try:
                self.commands[command](args)
            except Exception as e:
                print(f"Error executing command: {e}")
        else:
            print(f"Unknown command: {command}. Type 'help' for available commands.")
    
    def run(self):
        """Main agent loop"""
        print(f"Welcome to the {self.name} - Enhanced Interactive Assistant!")
        print("Type 'help' for available commands or 'quit' to exit.")
        
        try:
            while True:
                try:
                    user_input = input("\nAI Agent> ")
                    self.process_command(user_input)
                except KeyboardInterrupt:
                    print("\nReceived interrupt signal. Goodbye!")
                    break
                except EOFError:
                    print("\nEnd of input. Goodbye!")
                    break
        except Exception as e:
            print(f"Unexpected error: {e}")
            sys.exit(1)

def main():
    """Main function"""
    try:
        agent = AIAgent()
        agent.run()
    except Exception as e:
        print(f"Failed to start AI Agent: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()