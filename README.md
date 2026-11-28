# Python Beginner Practice

A collection of small Python projects for practicing Python fundamentals, file handling, CSV data, pandas, and basic chatbot behavior.

## Projects

| Project | Description |
| --- | --- |
| `Greet_bot` | Asks for a name and prints a personalized welcome message. |
| `Calculator` | Performs basic arithmetic and stores calculation history in a text file. |
| `Console_chatbot` | A keyword-based chatbot that analyzes a short list of student marks. |
| `Chat_bot` | A chatbot with persistent JSON history, date/time replies, and CSV student analysis. |
| `pandas_Practice` | Loads, cleans, analyzes, and exports a pandas student performance dataset. |

## Requirements

- Python 3.10 or newer
- `pandas`
- `python-dotenv`

Install the external packages with:

```bash
python -m pip install pandas python-dotenv
```

## Run a Project

Run commands from the repository root.

### Greeting Bot

```bash
python Greet_bot/greet_bot.py
```

Enter a name when prompted. Leaving the name empty prints a missing-name message.

### Calculator

```bash
python Calculator/Calculator.py
```

Supported operations:

- Addition
- Subtraction
- Multiplication
- Division
- Exponentiation
- Modulus
- View calculation history
- Clear calculation history
- Exit

History is stored in `calculation_history.txt` in the directory from which the script is run.

### Console Chatbot

```bash
python Console_chatbot/chatbot.py
```

Supported keywords include `hello`, `hi`, `name`, `python`, `help`, and `how are you`. Enter `bye` to end the chat and show the conversation and student marks summary.

### Persistent Chatbot

```bash
cd Chat_bot
python main.py
```

Commands:

- `history` - show previous chat messages
- `students` - analyze `students.csv`
- `bye` - end the conversation

Chat history is saved in `Chat_bot/chat_history.json`.

The chatbot name can be configured in `Chat_bot/.env`:

```text
BOT_NAME=PythonBot
```

The CSV must contain the columns `name`, `python`, `math`, and `english`.

### Pandas Practice

```bash
cd pandas_Practice
python main.py
```

This project:

- Loads `Dataset/StudentsPerformance.csv`
- Displays dataset information and missing values
- Removes duplicate rows
- Adds an average score and performance category
- Calculates grouped averages
- Finds high-performing students
- Saves the cleaned data as `clean.csv`

## Project Structure

```text
python_beginer_practice/
|-- Calculator/
|   `-- Calculator.py
|-- Chat_bot/
|   |-- chatbot.py
|   |-- main.py
|   |-- students.csv
|   `-- .env
|-- Console_chatbot/
|   `-- chatbot.py
|-- Greet_bot/
|   `-- greet_bot.py
|-- pandas_Practice/
|   |-- main.py
|   `-- Dataset/
|       `-- StudentsPerformance.csv
`-- README.md
```

## License

This repository is a personal Python practice project. No license is currently specified.
