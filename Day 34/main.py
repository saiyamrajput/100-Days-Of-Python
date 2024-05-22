from question_model import Question
from data import questions
from quiz_brain import QuizBrain
from ui import QuizInterface

# storing questions in question_banks
question_bank = []
for question in questions:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# creating quiz interface and quiz brain object
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

