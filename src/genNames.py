import random

import pandas as pd

# Read the CSV file
df = pd.read_csv('nomes.csv')

# Extract the 'first_name' column
first_names = df['first_name'].dropna().tolist()

# List of 20 kids' names
# kids_names = [
#     "Alice", "Ben", "Charlie", "Daisy", "Ethan", "Fiona", "George", "Hannah",
#     "Ian", "Julia", "Kevin", "Lily", "Michael", "Nina", "Oliver", "Paula",
#     "Quentin", "Rachel", "Samuel", "Tina"
# ]

kids_names = first_names

# List of 30 random usual actions in a playground
playground_actions = [
    "playing on the slide", "swinging on the swing", "running", "playing soccer",
    "playing hide and seek", "jumping rope", "playing in the sandbox",
    "playing dodgeball", "riding a bicycle", "playing with a ball", "talking",
    "reading a book", "having a picnic", "drawing on the ground with chalk",
    "climbing a tree", "playing tag", "building a sandcastle",
    "playing volleyball", "roller skating", "playing hopscotch",
    "playing with dolls", "watching a puppet show", "playing marbles",
    "playing cops and robbers", "going on a trail", "playing on the seesaw",
    "chasing a kite", "playing basketball", "playing ring-around-the-rosy",
    "having a sack race"
]

# Generate a list of kids with their random actions
kids_activities = []

for name in kids_names:
    action = random.choice(playground_actions)
    kids_activities.append(f"{name} is {action}")

# Print the list of kids and their activities
# for activity in kids_activities:
#     print(activity)
    
# Write the arrays to a text file
with open('kids_activities.txt', 'w') as file:
    for activity in kids_activities:
        file.write(''.join(map(str, activity)) + '\n')    
