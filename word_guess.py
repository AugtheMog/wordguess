def cover_word(word_to_guess):
    index = 0
    masked = ""
    while index < len(word_to_guess):
        masked = masked + "*"
        index += 1
    return masked

def uncover_mask(word_to_guess, letter_guess):
    unmasked_word = word_to_guess
    unmasked_word = list(word_to_guess)
    for letter in word_to_guess:
        unmasked_word
def check_word(word_to_guess, letter_guess):
    index = 0
    for letter in word_to_guess:
        if letter_to_guess == letter:
            uncover_mask(word_to_guess, letter_guess)

choice = input("Play the word guess?").lower()
word_to_guess = "Surprise"
mask_word = cover_word(word_to_guess)
print(mask_word)
letter_guess = input("Pick a letter the word might have: ")
letter_exists_in_word = check_word(word_to_guess, letter_guess)


