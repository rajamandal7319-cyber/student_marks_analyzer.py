import random
import string

print("===== PASSWORD GENERATOR =====")

length = int(input("Password ki length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password = password + random.choice(characters)

print("Your Password:", password)

print("Powered by : RAJ.K.M ©")