from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []
for question in question_data:
    text_q = question["text"]
    answer_q = question["answer"]
    new_q = Question(text_q, answer_q)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
