# import random
# import string

# def generate_password(length=8):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(random.choice(characters) for _ in range(length))
#     return password

# password_length =8          #if you want to take password length from user 
# generated_password = generate_password(password_length)
# print("Generated Password:", generated_password)




import string 
import random
def gen_pass(length=12):
    char=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(char)for _ in range(length))
    return password

password_length=int(input("Enter your password length:"))
generated_password=gen_pass(password_length)
print("Generated password:",generated_password)
