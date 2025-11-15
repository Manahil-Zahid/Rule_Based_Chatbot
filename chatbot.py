import re
import random

# Pattern-Response Pairs
pairs = [
    [r"hi|hello|hey", ["Hello! Hope your day is good.", "Hi there! How can i help you today?", "Hey! Nice to see you here."]],
    [r"my name is (.*)", ["Nice to meet you, %1! How can i assist you today?", "Hello %1, Hope you are having a great day!", "Hey %1, What can i do for you today?"]],
    [r"(.*) your name?", ["I'm your friendly chatbot!", "I'm a chatbot, Your friendly Assistant!"]],
    [r"how are you?", ["I'm doing well, thankyou! How about you?", "I'm good! How is your day going?"]],
    [r"tell me a joke", ["Why did the math book look sad? Because it had too many problems!", "Why did the scarecrow win an award? Because he was outstanding in his field!", "Why was the computer cold? It left its Windows open!"]],
    [r"bye|goodbye|see you", ["Goodbye! Have a great day!", "See you later! Take care!", "Bye! Hope to chat with you soon."]],
    [r"thank you|thanks|thanks alot", ["You're Welcome!", "No Problem! Happy to help.", "Anytime!"]],
    [r"what can you do", ["I can chat with you, tell jokes, answer questions, and assist with tasks!"]],
    [r"who created you", ["I was created by developers who love AI and coding."]],
    [r"good morning", ["Good morning! Hope you have a wonderful day ahead!"]],
    [r"good night", ["Good night! Sweet dreams."]],
    [r"what is your purpose?", ["I’m here to help you and make your day easier!"]],
    [r"(.*)", ["I'm not sure I understand. Can you rephrase?", "Sorry! I didn't get that. Could you try saying it differently?", "Hmm, I'm not sure about that."]]
]

# Function to get chatbot response
def respond(user_input):
    user_input = user_input

    for pattern, responses in pairs:
        match = re.match(pattern, user_input, re.IGNORECASE)

        if match:
            response = random.choice(responses)

            # Replace %1, %2, %3 with captured groups
            for i in range(len(match.groups())):
                response = response.replace(f"%{i+1}", match.group(i+1) or "")

            return response

    return "Sorry, I don't understand."


# Main chat loop
print("ChatBuddy: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ")

    if user.lower() in ["bye", "goodbye", "see you"]:
        print("ChatBuddy: Goodbye! Have a great day!")
        break

    print("ChatBuddy:", respond(user))
