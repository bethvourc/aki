# Akinator-like Game Project

## Overview
This project is a Python-based interactive guessing game, inspired by the popular Akinator game. It uses Pygame for the graphical user interface and SQLite for managing a database of questions and answers. The game intelligently guesses characters or objects based on the user's answers to a series of questions.

## Features
- **Graphical User Interface**: Built with Pygame for an engaging user experience.
- **Voice Recognition**: Users can respond to questions using voice commands.
- **SQLite Database Integration**: Questions and answers are managed through a SQLite database for easy updating and maintenance.
- **Scalable Question Logic**: Advanced logic for question selection, potentially integrating machine learning in future updates.
- **Localization**: Planned support for multiple languages.

## Installation

### Prerequisites
- Python 3.x
- Pygame
- SQLite3
- SpeechRecognition (for voice recognition feature)

### Setup
1. Clone the repository:
   ```
   git clone https://github.com/bethvourc/akinator-game.git
   ```
2. Install the required packages:
   ```
   pip install pygame sqlite3 SpeechRecognition
   ```

## Usage
Run the game by executing the main script:
```
python akinator.py
```

## How to Play
- Start the game and wait for the first question.
- Answer each question by speaking 'yes' or 'no' into your microphone.
- The game will attempt to guess what you are thinking of based on your answers.

## Contributing
Contributions to this project are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`.
3. Make your changes and commit them: `git commit -m 'commit message'`.
4. Push to the original branch: `git push origin your-project-name/feature-branch-name`.
5. Create the pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://help.github.com/articles/creating-a-pull-request/).

## License
This project is licensed under the [MIT License](LICENSE.md).
