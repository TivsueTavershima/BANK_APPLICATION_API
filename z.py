import random

account_number = ''.join([str(random.randint(0, 9)) for _ in range(10)])
print(account_number) 