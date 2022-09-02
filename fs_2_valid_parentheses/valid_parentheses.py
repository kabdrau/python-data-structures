def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    count = 0
    if parens[0] == '(' and parens[-1] == ')' and len(parens) % 2 == 0:
        for p in parens:
            if p == '(':
                count += 1
            if p == ')':
                count -= 1
        if count == 0:
            return True
    return False