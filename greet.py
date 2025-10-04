import os

env = os.getenv("ENV")
msg = os.getenv("MESSAGE")

print(f"Environment: {env}")
print(f"Greeting: {msg}")