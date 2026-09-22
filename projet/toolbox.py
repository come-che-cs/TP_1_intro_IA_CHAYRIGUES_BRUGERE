def is_palindrome(s: str) -> bool:
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

def word_frequency(text: str) -> dict:
    import string
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    words = text.split()
    return {word: words.count(word) for word in set(words)}


def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 9/5 + 32