import hangman_function as hg

########################## GAME ########################

hg.welcome_message()

#variables initialization
hidden_word, num_attempts, missed_letters, guessed_letters, discovered_word, hidden_word_char, counter = hg.initialize()

hg.initial_hint(hidden_word_char)

while num_attempts != 0 and not discovered_word:

    user_letter = hg.new_attempt(num_attempts)

    is_valid = hg.valid_letter(user_letter,guessed_letters,missed_letters)

    #if letter is on the word
    if  is_valid and user_letter in hidden_word and user_letter not in guessed_letters:
        print("You're right!")
        guessed_letters.append(user_letter)

        letter_index = hg.index_character(hidden_word, user_letter)
        hidden_word_char = hg.replace_char(hidden_word_char, letter_index, user_letter)

        if hidden_word == hidden_word_char:
            discovered_word = True

    #if letter is wrong
    elif is_valid and user_letter not in hidden_word and user_letter not in missed_letters:

        print("This letter is not in the word!")
        missed_letters.append(user_letter)

        hg.print_letters(missed_letters)

        num_attempts -= 1
        counter += 1

        hg.draw_Hangman(counter)

    #if letter is not valid
    elif not is_valid:
        continue

    hg.print_word_status(hidden_word_char)

    hg.winner_loser(discovered_word,num_attempts)




