def find_first_occurance(
    larger_text,
    smaller_text):

    larger_text_length = len(larger_text)
    smaller_text_length = len(smaller_text)

    for starting_position in range(
        larger_text_length - smaller_text_length + 1):
        # Iterate through all possible starting positions
        # within the larger text.

        match = True
        for character_index in range(smaller_text_length):
            if larger_text[starting_position + \
                    character_index] != \
                    smaller_text[character_index]:
                match = False
                break

        # If all characters match, return
        # the starting position.
        if match:
            return starting_position

    # If no match is found, return -1.
    return -1
