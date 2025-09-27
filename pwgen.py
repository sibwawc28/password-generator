import string
import secrets

print("Welcome to Password Generator, queen ")
print("How many letters do you want in your password ")
numof=int(input())

lower= string.ascii_lowercase   #not (), cuz they're not functions but constants
upper= string.ascii_uppercase
all=string.ascii_letters
num=string.digits
punct=string.punctuation

total=all+num+punct

password=""
for i in range(numof):
    password=secrets.choice(total) + password

print(password)