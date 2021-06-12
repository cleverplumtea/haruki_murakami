def sentence_counter(text):
    counter = 0
    for i in range(0, len(text)):
        if text[i] == "." or text[i] == "!" or text[i] == "?":
            counter += 1
    return counter
