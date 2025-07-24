import random

# 🖼 Array of ASCII art diagrams
ascii_art_diagrams = [
    r"""
     /\_/\
    ( o.o )
     > ^ <
    """,

    r"""
     _______
    |       |
    |       O
    |      /|\
    |      / \
    |
    =========
    """,

    r"""
    _______
   /       \
  |  (• ◡•)  |
   \_/
    """,

    r"""
     __
    /  \
   |    |
   ||
  /      \
 /\
    """
]

# 📝 Array of creative writing prompts
story_prompts = [
    "Write a story about a robot who wants to be human.",
    "Describe a world where plants can talk to people.",
    "Create a mystery involving a time-traveling detective.",
    "Tell a bedtime story set on a spaceship.",
    "Imagine a dragon who’s afraid of fire.",
    "Write about a kid who finds a magical notebook.",
    "Narrate a short poem about loneliness and the moon.",
    "Describe an ancient civilization powered by sound."
]

#Main Loop
while True:
    user_input =input('\n Type "draw", "write", or "exit": ').strip().lower()

    if user_input == "exit":
        print('👋Goodbye')
        break
    elif user_input.startswith("draw"):
        selected_art = random.choice(ascii_art_diagrams)
        print(selected_art)
        
    elif user_input.startswith("write"):
        selected_prompt = random.choice(story_prompts)
        print('\n 📝Here\'s a random creative writing prompt:')
        print(selected_prompt)
    
    else:
        print('❌ Invalid input. Please type "draw", "write", or "exit".')