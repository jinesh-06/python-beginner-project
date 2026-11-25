def greet(name: str) -> str:
    name = name.strip()
    if name:
        return f"Hello, {name}! Nice to meet you."
    return "Hello there! Nice to meet you."


def main() -> None:
    print("Hi! I'm your greeting bot.")
    name = input("What's your name? ")
    print(greet(name))


if __name__ == "__main__":
    main()