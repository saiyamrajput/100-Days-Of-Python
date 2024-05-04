# import statements
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# printing the welcome message
print("Welcome!!\nLet's start the Quiz.\n")
# question_bank stores all the questions and answers from the data.py module
question_bank = []

# extracting questions and answers and adding them in question_bank
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# creating object to run the quiz
quiz = QuizBrain(question_bank)

# starting the quiz
while quiz.still_has_questions():
    quiz.next_question()

# displaying end message with total score
print("\nThank you for completing the quiz😊🎉")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
