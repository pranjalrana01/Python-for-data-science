### this project made fake news using random words
#-------------------------------------------------------------------

import random

subjects = [
    "Shahrukh khan",
    "Virat Kohli",
    "Rohit Sharma",
    "Group of monkeys",
    "prime minister modi",
    "auto rickshaw driver from delhi"
]

actions = [
    "launches",
    "cancels party",
    "declares war on",
    "celebrates",
    "orders"
]

places_or_things = [
    "at red fort",
    "in mumbai local train",
    "inside parliament",
    "played cricket well",
    "dances in magic show",
    "cooks food on streets"
]


while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)

    user_input = input("\ndo you want another headline? (yes/no)").strip().lower()
    if user_input == "no":
        break

print("\nThanks for using the fake news generator...!")