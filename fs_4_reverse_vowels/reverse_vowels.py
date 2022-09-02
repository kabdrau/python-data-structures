def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = 'uoiea'
    s_lst = list(s)
    vowels_lst = []
    i = 0
    for el in s_lst:
        i += 1
        if el.lower() in vowels:
            vowels_lst.append(el)
            s_lst[i-1] = "temp"
    vowels_lst.reverse()
    j = 0
    for el in s_lst:
        j += 1
        if el == 'temp':
            s_lst[j-1] = vowels_lst[0]
            vowels_lst.pop(0)
    return ("".join(str(x) for x in s_lst))