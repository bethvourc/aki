from flask import Flask, render_template, request, jsonify
import sqlite3
import random

app = Flask(__name__)

def setup_database():
    with sqlite3.connect('questions.db') as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS questions
                     (id INTEGER PRIMARY KEY, question TEXT, yes INTEGER, no INTEGER)''')
        example_questions = [
            (1, "Is your character real?", 2, 3),
            (2, "Is your character a famous athlete?", None, None),
            (3, "Is your character from a TV show?", None, None),
        ]
        c.executemany('INSERT OR IGNORE INTO questions VALUES (?,?,?,?)', example_questions)
        conn.commit()

def load_questions():
    with sqlite3.connect('questions.db') as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM questions')
        questions = {str(row[0]): {"question": row[1], "yes": row[2], "no": row[3]} for row in c.fetchall()}
    return questions

@app.route('/')
def index():
    questions = load_questions()
    first_question_id = random.choice(list(questions.keys()))
    first_question = questions[first_question_id]['question']
    return render_template('index.html', question=first_question, question_id=first_question_id)

@app.route('/answer', methods=['POST'])
def answer():
    data = request.json
    question_id = data['question_id']
    answer = data['answer']
    questions = load_questions()
    next_question_id = questions[question_id][answer]
    
    if next_question_id is not None and str(next_question_id) in questions:
        next_question = questions[str(next_question_id)]['question']
        return jsonify({"question": next_question, "question_id": str(next_question_id)})
    else:
        # Implement your logic for when the game ends or restarts
        return jsonify({"question": "Game Over. Restart?", "question_id": "restart"})

if __name__ == '__main__':
    setup_database()  # Ensure the database is setup
    app.run(debug=True)
