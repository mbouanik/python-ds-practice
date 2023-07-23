def single_letter_count(word, letter):
    count = 0
    for char in word.lower():
        if char == letter.lower():
            count += 1
    return count
