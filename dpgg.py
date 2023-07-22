def main():
    print("Welcome to the Disney Princess Guessing Game!")
    name = input("What is your name? ")
    favorite_color = input("What is your favorite color? ")
    self_description = input("Choose one word to describe yourself: ")

    # Dictionary with characteristics of each Disney princess
    princesses = {
        "Cinderella": {"color": "blue", "description": "kind"},
        "Ariel": {"color": "green", "description": "curious"},
        "Belle": {"color": "yellow", "description": "intelligent"},
        "Snow White": {"color": "red", "description": "cheerful"},
        "Jasmine": {"color": "purple", "description": "adventurous"},
    }

    # Guessing logic based on favorite color and self description
    guessed_princess = None

    for princess, traits in princesses.items():
        if favorite_color.lower() == traits["color"] and self_description.lower() == traits["description"]:
            guessed_princess = princess
            break

    if guessed_princess:
        print(f"\nHello, {name}! Based on your favorite color and self-description, you might be {guessed_princess}.")
    else:
        print("\nSorry, we couldn't find a matching Disney princess for you.")

if __name__ == "__main__":
    main()
