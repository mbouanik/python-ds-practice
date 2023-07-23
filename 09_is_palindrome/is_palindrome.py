def is_palindrome(phrase):
    phrase = "".join(phrase.lower().split())
    i = 0
    j = len(phrase) -1
    while i < j:
        if phrase[i] != phrase[j]:
            return False
        i += 1
        j -= 1
    return True
