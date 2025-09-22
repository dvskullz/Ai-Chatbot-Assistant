from word2number import w2n

# Mapping for math words to symbols
math_symbols_mapping = {
    "plus": "+",
    "add": "+",
    "minus": "-",
    "subtract": "-",
    "times": "*",
    "multiplied": "*",
    "multiply": "*",
    "divided": "/",
    "divide": "/",
    "over": "/",
    "mod": "%",
    "modulo": "%",
    "power": "**",
    "to the power of": "**"
}

def replace_words_with_numbers(transcript):
    transcript_with_numbers = ''
    for word in transcript.split():
        try:
            number = w2n.word_to_num(word)
            transcript_with_numbers += ' ' + str(number)
        except ValueError:
            transcript_with_numbers += ' ' + word
    return transcript_with_numbers

def clear_transcript(transcript):
    cleaned_transcript = ''
    for word in transcript.split():
        if word.isdigit():
            cleaned_transcript += word
        elif word in math_symbols_mapping.values():
            cleaned_transcript += word
        else:
            cleaned_transcript += math_symbols_mapping.get(word, '')
    return cleaned_transcript

def calculate(expression):
    """
    Supports: 'one plus two', '3 + 4', 'seven times five', etc.
    """
    transcript_with_numbers = replace_words_with_numbers(expression)
    math_equation = clear_transcript(transcript_with_numbers)
    try:
        result = str(eval(math_equation))
        return result
    except Exception as e:
        return f"Sorry, I couldn't calculate that. {e}"