from counter.reading_level import index
from counter.characters import character_counter
from counter.words import word_counter
from counter.sentences import sentence_counter
from counter.paragraphs import paragraph_counter
from counter.bigrams import bigram_counter
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
  if request.method == 'POST':
    text = request.form.get('text').strip()

    characters = character_counter(text)
    words = word_counter(text)
    paragraphs = paragraph_counter(text)
    sentences = sentence_counter(text)
    bigrams = bigram_counter(text)
    reading_level = 0

    if characters > 100:
      reading_level = index(text)

    if character_counter(text) == 0:
      return render_template('index.html')
    else:
      return render_template('index.html', coleman_liau_index = reading_level, characters = characters, words = words, paragraphs = paragraphs, sentences = sentences, bigrams = bigrams)
  else:
    return render_template('index.html')
