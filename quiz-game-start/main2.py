from question_model import Question
from data2 import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    # print(question)
    # print(question["text"])
    # print(question["answer"])
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# for x in range(len(question_bank)):     # debug
#     print(question_bank[x].text)
#     print(question_bank[x].answer)

quiz = QuizBrain(question_bank)      # new quiz
while quiz.still_has_questions():
    quiz.next_question()

print(f"Your final score is {quiz.score}.")
