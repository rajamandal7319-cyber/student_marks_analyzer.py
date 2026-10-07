print("===== QUIZ GAME =====")

questions = [
    "Python kis type ki language hai?",
    "2 + 2 kitna hota hai?",
    "HTML ka full form kya hai?",
    "Python file ka extension kya hota hai?",
    "CPU ka full form kya hai?"
]

answers = [
    "programming",
    "4",
    "hypertext markup language",
    "py",
    "central processing unit"
]

score = 0

for i in range(len(questions)):
    print("\nQuestion", i + 1)
    print(questions[i])

    answer = input("Answer: ").lower()

    if answer == answers[i]:
        print("Correct! ✅")
        score = score + 1
    else:
        print("Wrong! ❌")
        print("Correct answer:", answers[i])

print("\n===== QUIZ FINISHED =====")
print("Your Score:", score, "/", len(questions))

print("Powered by : RAJ.K.M ©")