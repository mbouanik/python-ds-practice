def multiple_letter_count(phrase):
    count = {}
    for letter in phrase:
        count[letter] = count.get(letter, 0) + 1
    return count
