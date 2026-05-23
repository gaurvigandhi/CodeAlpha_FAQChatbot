questions = ["hello", "fees", "course", "certificate"]

answers = [
    "Hello!",
    "Course fee is ₹10,000.",
    "We offer Python courses.",
    "Yes, certificate is provided."
]

while True:
    user = input("You: ").lower()

    if user == "bye":
        print("Bot: Goodbye!")
        break

    if user in questions:
        index = questions.index(user)
        print("Bot:", answers[index])

    else:
        print("Bot: Sorry, I don't understand.")