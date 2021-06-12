def paragraph_counter(text):
    counter = 0
    for i in range(0, len(text)):
        if text[i] == '\n':
            counter += 1
    return int((counter / 2) + 1)
