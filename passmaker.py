import random 
import string 

letters = string.ascii_letters
digits = string.digits
symbols = "£*)!/=-$%"

all_chars = letters + digits + symbols

length = int(input("How long do you want your password?"))

password = "".join(random.choice(all_chars) for _ in range(length))
print("Your new password is... this:", password)
