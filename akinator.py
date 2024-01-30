import pygame
import sqlite3
import random

# Initialize Pygame
pygame.init()

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE, BLACK = (255, 255, 255), (0, 0, 0)

# Database Setup
def setup_database():
    conn = sqlite3.connect('questions.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS questions
                 (id INTEGER PRIMARY KEY, question TEXT, yes INTEGER, no INTEGER)''')

    # Example Question Insertion
    # You should replace this with your actual questions
    example_questions = [
        (1, "Is your character real?", 2, 3),
        (2, "Is your character a famous athlete?", None, None),
        (3, "Is your character from a TV show?", None, None),
    ]

    c.executemany('INSERT OR IGNORE INTO questions VALUES (?,?,?,?)', example_questions)
    conn.commit()
    conn.close()

setup_database()

# Load the questions and answers from the database
def load_questions():
    conn = sqlite3.connect('questions.db')
    c = conn.cursor()
    c.execute('SELECT * FROM questions')
    questions = {str(row[0]): {"question": row[1], "yes": row[2], "no": row[3]} for row in c.fetchall()}
    conn.close()
    return questions

questions = load_questions()

# Initialize the game window
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Akinator Game")

# Akinator class
class Akinator:
    def __init__(self, questions):
        self.questions = questions
        self.current_question = random.choice(list(questions.keys()))
        self.answered_questions = {}

    def display_question(self):
        question_text = self.questions[self.current_question]["question"]
        font = pygame.font.Font(None, 30)
        text = font.render(question_text, True, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        win.blit(text, text_rect)

    def process_answer(self, answer):
        self.answered_questions[self.current_question] = answer
        next_question_id = self.questions[self.current_question][answer]
        
        if next_question_id and str(next_question_id) not in self.answered_questions:
            self.current_question = str(next_question_id)
        else:
            # Here you could implement logic to make a guess based on answered questions
            # For now, it just restarts the game
            self.current_question = random.choice(list(self.questions.keys()))
            self.answered_questions = {}

    def play(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        self.process_answer('yes')
                    elif event.key == pygame.K_n:
                        self.process_answer('no')

            win.fill(WHITE)
            self.display_question()
            pygame.display.update()

        pygame.quit()

# Create an instance of the Akinator game and start the game
akinator = Akinator(questions)
akinator.play()

