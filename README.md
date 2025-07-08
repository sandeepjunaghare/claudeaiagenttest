# AI Agent - Interactive Assistant

A simple interactive AI assistant that provides basic functionality through a command-line interface.

## Features

- **Interactive Command Interface**: Type commands and get responses
- **Time Display**: Get current date and time
- **Echo Service**: Echo back messages
- **Calculator**: Perform basic mathematical calculations
- **Help System**: Built-in help for all commands
- **Error Handling**: Robust error handling for invalid input

## Usage

### Running the Agent

```bash
python3 main.py
```

### Available Commands

- `help` - Show available commands
- `time` - Display current time
- `echo <message>` - Echo back your message
- `calculate <expression>` - Calculate a math expression
- `quit` or `exit` - Exit the agent

### Example Session

```
Welcome to the AI Agent - Enhanced Interactive Assistant!
Type 'help' for available commands or 'quit' to exit.

AI Agent> help

AI Agent v1.0.0 - Available commands:
  help - Show this help message
  time - Display current time
  echo <message> - Echo back your message
  calculate <expression> - Calculate a math expression
  quit/exit - Exit the agent

AI Agent> time
Current time: 2024-01-15 14:30:25

AI Agent> echo Hello World
Echo: Hello World

AI Agent> calculate 2 + 3 * 4
Result: 2 + 3 * 4 = 14

AI Agent> quit
Goodbye!
```

## Security Features

- Input validation for mathematical expressions
- Only basic math operations allowed in calculator
- Proper error handling for invalid commands
- Safe exit handling for keyboard interrupts

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Project Structure

```
.
├── main.py       # Main AI agent application
└── README.md     # Project documentation
```

## Version History

- v1.0.0 - Initial release with basic interactive functionality
- Earlier versions - Simple greeting message only

## Bug Fixes Applied

1. **Removed unused files**: Cleaned up temporary `notes.txt` file
2. **Added actual functionality**: Transformed from simple greeting to interactive agent
3. **Added error handling**: Comprehensive exception handling throughout
4. **Added documentation**: Complete README with usage instructions
5. **Fixed misleading project description**: Now actually functions as an AI agent

## Contributing

This is a simple educational project. Feel free to extend it with additional commands and features.

## License

This project is provided as-is for educational purposes.