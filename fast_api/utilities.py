import random
import string

punctuation = '@$!%*#?&'

def generate_secret(size=8, is_password=False):
  if size<4:
    raise ValueError(f"Invalid secret size: {size}")
  # Set of characters to choose from
  chars = string.ascii_letters + string.digits + (punctuation if is_password else "")
  
  # Generate a random secret
  secret = random.choice(string.ascii_lowercase)
  secret += random.choice(string.ascii_uppercase)
  secret += random.choice(string.digits)
  secret += random.choice(punctuation) if is_password else ""
  for i in range(size - len(secret)):
      secret += random.choice(chars)
  
  # Shuffle the secret
  secret_list = list(secret)
  random.shuffle(secret_list)
  secret = ''.join(secret_list)
  
  return secret