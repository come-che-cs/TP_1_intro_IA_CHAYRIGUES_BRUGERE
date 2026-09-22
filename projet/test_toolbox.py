from toolbox import is_palindrome, word_frequency

def test_is_palindrome_simple():
    assert is_palindrome("radar") is True


def test_is_palindrome_with_spaces():
    assert is_palindrome("un roc si biscornu") is True  # échoue à cause du bug


def test_is_palindrome_false():
    assert is_palindrome("python") is False


def test_word_frequency_simple():
    assert word_frequency("chat chat chien") == {"chat": 2, "chien": 1}


def test_word_frequency_insensible_a_la_casse():
    assert word_frequency("Chat CHAT chat") == {"chat": 3}


def test_word_frequency_ignore_la_ponctuation():
    assert word_frequency("chat, chien. chat!") == {"chat": 2, "chien": 1}


def test_word_frequency_espaces_et_retours_a_la_ligne():
    text = "un  deux\nun\tdeux\n trois"
    assert word_frequency(text) == {"un": 2, "deux": 2, "trois": 1}


def test_word_frequency_phrase_complete():
    text = "Le le LE\nchat et le chien"
    assert word_frequency(text) == {"le": 4, "chat": 1, "et": 1, "chien": 1}


def test_word_frequency_vide():
    assert word_frequency("") == {}
