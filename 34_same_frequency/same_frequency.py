def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    lst1 = [int(x) for x in str(num1)]
    lst1.sort()
    lst2 = [int(x) for x in str(num2)]
    lst2.sort()
    return lst1 == lst2