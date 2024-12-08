#QuizContent = [{"Question":"What is the element F?", "Answers" : ["1. Hydrogen", "2. Flourine"], "Correct" : "2"}]
import json

with open ("questions.json", "r") as file:
    content = file.read()

data = json.loads(content)

UserAnswer = []
CorrectAnswer = []
response = []

for Questions in data:
    print (f"{Questions['Question']} \n  {Questions['Answers']}")
    user_answer = int(input("Select the right option: "))

    response.append((user_answer, Questions["Correct"]))

score = 0
for index, r in enumerate(response):
#    print (r)
    print ("#############################################")
    print (f"Question- {index + 1}")
#    print (f"User Answer: {r[0]}")
#    print  (f"Correct Answer: {r[1]}")
    if r[0] == int(r[1]):
        score = score +1 

print (f"Total Score is {score} of {len(response)}")



