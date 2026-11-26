import time

print("=" * 10, "Greeting Bot", "=" * 10)

name = input("Enter your name: ").strip()

if name:
    print(f"\nHello, {name}!")
    time.sleep(1)
    print(f"Welcome, {name}, to Python programming!")
    print("Hope you have a great day!")
else:
    print("You forgot to enter your name!")