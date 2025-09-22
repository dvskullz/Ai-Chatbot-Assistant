import random

import random

# Global joke list and tracker
jokes = [
    "Why did the computer show up at work late? It had a hard drive!",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the scarecrow get a promotion? He was outstanding in his field!",
    "Why do Java developers wear glasses? Because they don’t see C#.",
    "Why was the math book sad? Because it had too many problems.",
    "Why don’t scientists trust atoms? Because they make up everything!",
    "Why did the bicycle fall over? Because it was two-tired!",
    "Why did the coffee file a police report? It got mugged!",
    "Why don’t skeletons fight each other? They don’t have the guts.",
    "Why was the computer cold? It left its Windows open!",
]

# Shuffle once at program start
random.shuffle(jokes)
joke_index = 0

def tell_joke():
    global joke_index
    global jokes
    # Pick current joke
    msg = jokes[joke_index]
    # Move to next joke
    joke_index += 1
    if joke_index >= len(jokes):
        random.shuffle(jokes)  # reshuffle after all jokes used
        joke_index = 0
    return msg


def tell_quote():
    quotes = [
        "The best way to get started is to quit talking and begin doing. – Walt Disney",
        "Success is not in what you have, but who you are. – Bo Bennett",
        "The impediment to action advances action. What stands in the way becomes the way.",
        "Happiness depends upon ourselves.",
        "What we think, we become.",
        "Do not go where the path may lead, go instead where there is no path and leave a trail.",
        "Simplicity is the ultimate sophistication.",
        "He who opens a school door, closes a prison.",
        "In the middle of every difficulty lies opportunity.",
        "An unexamined life is not worth living.",
        "The harder you work for something, the greater you’ll feel when you achieve it."
    ]
    return random.choice(quotes)