from random import randint
from data import Question, questions_answers_full

print("\n" * 20)
print("Welcome to the Orientation AI Quizz!")
print("There are 10 questions. Type 'A', 'B', 'C' or 'D'. ")
print("\n")
score = 0

def check_answer(user_answer, correct_answer, question_number):
    if user_answer.lower() == correct_answer.lower(): 
        global score
        score += 1
        print("You got it right!")
    else:
        print(f"You got it wrong! The correct answer was: {questions_answers_full[question_number]["answer"]}")
    print("\n")

which_questions = list()
for i in range(10):
    which_questions.append(randint(1, 100))

for i in which_questions:
    print(f"Question nr {i + 1}: ")
    print(questions_answers_full[i]["question"])
    print(f"A) {questions_answers_full[i]["A"]}")
    print(f"B) {questions_answers_full[i]["B"]}")
    print(f"C) {questions_answers_full[i]["C"]}")
    print(f"D) {questions_answers_full[i]["D"]}")
    print(f"E) {questions_answers_full[i]["E"]}")

    user_guess = input(f"Your answer: ")
    check_answer(user_guess, questions_answers_full[i]["answer"], i)
    
print(f"Congratulations! You got {(score/10) * 100}%")
