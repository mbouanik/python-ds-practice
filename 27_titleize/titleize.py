def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    res = []
    for word in phrase.lower().split():
        res.append(word[0].upper() + word[1:])
    return " ".join(res)
