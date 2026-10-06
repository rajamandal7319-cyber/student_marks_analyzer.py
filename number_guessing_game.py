import random

number = random.randint(1, 10)

print("===== NUMBER GUESSING GAME =====")
print("Maine 1 se 10 ke beech ek number choose kiya hai.")
print("Tumhare paas 3 attempts hain.")

attempts = 1
score = 0

while attempts <= 3:
    guess = int(input("Number guess karo: "))

    if guess == number:
        print("Correct! Tum jeet gaye!")
        score = 100
        break
    elif guess < number:
        print("Too low! Thoda bada number try karo.")
    else:
        print("Too high! Thoda chhota number try karo.")

    attempts = attempts + 1

if attempts > 3:
    print("Game Over! 3 attempts khatam.")
    print("Correct number was:", number)

print("Your Score:", score)
print("===== GAME FINISHED =====")
print("Powered by : RAJ.K.M ©")