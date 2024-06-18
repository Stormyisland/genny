import random 




uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
numbers = "1234567890"
symbols = "~!@#$%^&*()_+=`?><{][]}`"

string = uppercase_letters + lowercase_letters +  numbers + symbols
length = 18 
password = "".join(random.sample(string,length ))

print(" "" ""\n Your new password is: \n" + password + "\n" + "dont forget it")
