def character_counter(text):
    counter = 0
    for i in range(0, len(text)):
        if text[i].isalpha():
            counter += 1
    return counter
