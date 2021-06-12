def bigram_counter(text):
  bigrams_set = set()
  for i in range(len(text.split()) - 1):
      bigrams_set.add((text[i], text[i + 1]))
  return len(bigrams_set)
