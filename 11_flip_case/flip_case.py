def flip_case(phrase, to_swap):
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

