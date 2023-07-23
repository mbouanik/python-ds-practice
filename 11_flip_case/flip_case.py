def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    fliped_case = ""
    for letter in phrase:
        if letter.lower() == to_swap.lower():
            if letter >= 'a' and letter <= 'z':
                fliped_case += letter.upper()
            else:
                fliped_case += letter.lower()
        else:
            fliped_case += letter
    return fliped_case 

