import json
from intent_match import IntentMatcher
from preprocess import preprocess_text  # Add this import if you have a preprocess module

try:
    with open("responses.json", "r") as file:
        data = json.load(file)
except FileNotFoundError:
    print("responses.json file not found. Please make sure it exists in the current directory.")
    exit(1)
except json.JSONDecodeError:
    print("responses.json is not a valid JSON file. Please fix its contents.")
    exit(1)

patterns = [item["pattern"] for item in data]
responses = [item["response"] for item in data]

# Preprocess patterns for better matching
preprocessed_patterns = [preprocess_text(p) for p in patterns]

# Pass both original and preprocessed patterns to the matcher
matcher = IntentMatcher(patterns, preprocessed_patterns)

print("Chatbot is ready! Type 'bye' to exit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "exit", "quit"]:
        print("Bot: Goodbye!")
        break

    processed_input = preprocess_text(user_input)
    index, score = matcher.match(processed_input)

    if index is None or score < 0.3:
        print("Bot: Sorry, I didn't understand that.")
    else:
        print("Bot:", responses[index])