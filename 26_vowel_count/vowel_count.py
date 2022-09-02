def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = 'aeiou'
    count_vowels = {}
    for char in phrase.lower():
        if char in vowels:
            if char in count_vowels:
                count_vowels[char] += 1
            else:
                count_vowels[char] = 1
    return count_vowels