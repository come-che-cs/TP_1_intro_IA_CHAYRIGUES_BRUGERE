import string
from collections import Counter

# Table pour is_palindrome : retire espaces, ponctuation, garde uniquement les alphanumériques
_remove_space_punct = str.maketrans('', '', string.whitespace + string.punctuation)
# Table pour word_frequency : retire uniquement la ponctuation (garde les espaces)
_remove_punct = str.maketrans('', '', string.punctuation)


def is_palindrome(s: str) -> bool:
    """Vérifie si la chaîne est un palindrome (ignore espaces et ponctuation)."""
    cleaned = s.translate(_remove_space_punct).lower()
    return cleaned == cleaned[::-1]


def word_frequency(text: str) -> dict:
    """Retourne la fréquence de chaque mot dans le texte (minuscule, sans ponctuation)."""
    cleaned = text.translate(_remove_punct).lower()
    words = cleaned.split()
    return dict(Counter(words))


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convertit une température de Celsius à Fahrenheit."""
    return celsius * 9 / 5 + 32
