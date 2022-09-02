def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    ltr_freq = {}
    for char in phrase:
        if char in ltr_freq:
            ltr_freq[char] += 1
        else:
            ltr_freq[char] = 1
    return ltr_freq