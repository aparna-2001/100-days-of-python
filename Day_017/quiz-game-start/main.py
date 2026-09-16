from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    new_question = Question(text=item['question'], answer=item['correct_answer'])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
        quiz.next_question()

print("you have completed the quiz")
print(f"your final score was {quiz.score/quiz.question_number}")