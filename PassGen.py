import string, secrets

letters = string.ascii_letters
punctuation = string.punctuation
digits = string.digits

code = letters + punctuation + digits
psw_length = int(input("How long should be the pass? (only digits): "))
pwd = ''
for i in range(psw_length):
    pwd += ''.join(secrets.choice(code))
print(pwd)






