# sys is a module. It lets us access command line arguments, which are
# stored in sys.argv.
import sys
import random

if len(sys.argv) < 2:
    print("Please supply a flash card file.")
    exit(1)

flashcard_filename = sys.argv[1]
f = open(flashcard_filename, "r")

que_ans = {}

for line in f:
    entry = line.strip().split(",")
    question = entry[0]
    answer = entry[1]
    que_ans[question] = answer

f.close()

questions = list(que_ans.keys())

print("Welcome to the flash card quiz!")
print("You can enter 'quit' at anytime to exit the game")

while True:
    ques = random.choice(questions)
    answ = que_ans[ques]
    choice = input(ques + "?")

    if choice == "quit":
        break
    elif choice == answ:
        print("you are correct!")
    else:
        print("oops! the answer is " + answ)
